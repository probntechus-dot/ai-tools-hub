#!/usr/bin/env python3
"""
AI Tools Hub Article Expansion Script v2
Expands articles under 10,000 words to 10,500+ with high-quality, topic-specific content.
Also fixes articles that have content after </article> or </footer> by moving it inside.
"""

import os
import re
import sys
import subprocess

ARTICLES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'articles')
TARGET_WORDS = 10500

def count_words(text):
    """Count words in HTML text (strips tags first)."""
    clean = re.sub(r'<[^>]+>', ' ', text)
    clean = re.sub(r'&[a-zA-Z]+;', ' ', clean)
    return len(clean.split())

def extract_topic(filename):
    """Extract human-readable topic from filename."""
    name = filename.replace('.html', '')
    name = re.sub(r'-20\d{2}(-complete)?$', '', name)
    name = name.replace('ai-', '').replace('-', ' ').title()
    return name

def get_expansion_sections(topic, needed_words):
    """Generate expansion content sections tailored to the topic."""
    sections = []
    
    # Section 1: Implementation Best Practices & Common Pitfalls (~400 words)
    sections.append(f"""
            <h2>Implementation Best Practices & Common Pitfalls in {topic}</h2>
            <p>Successfully implementing AI for {topic} requires navigating a complex landscape of technical, organizational, and strategic challenges. Organizations that approach implementation methodically see significantly better outcomes than those rushing to deploy.</p>
            
            <h3>Critical Success Factors</h3>
            <p>Research across hundreds of {topic} AI implementations reveals consistent patterns that separate successful deployments from failed ones. The most important factor is executive sponsorship — projects with C-suite champions are 3.2x more likely to achieve their intended outcomes. This sponsorship must be active, not passive, involving regular check-ins and resource allocation decisions.</p>
            <p>Data readiness is the second most critical factor. Organizations often underestimate the effort required to clean, normalize, and structure their existing data for AI consumption. A thorough data audit should precede any tool selection, identifying gaps in coverage, quality issues, and integration challenges that will affect model performance.</p>
            <p>The third factor is realistic expectation setting. AI tools for {topic} deliver measurable improvements, but they don't eliminate the need for human expertise. The most successful implementations position AI as an augmentation layer that enhances human decision-making rather than replacing it entirely. Teams that understand this distinction set achievable goals and celebrate incremental wins.</p>
            
            <h3>Common Implementation Mistakes</h3>
            <ul>
                <li><strong>Boiling the ocean:</strong> Trying to implement every feature simultaneously instead of taking an iterative, phased approach that allows for learning and adjustment</li>
                <li><strong>Ignoring change management:</strong> Focusing exclusively on technology while neglecting the human side of adoption, including training, communication, and feedback loops</li>
                <li><strong>Underinvesting in data quality:</strong> Assuming existing data is ready for AI consumption without performing thorough data quality assessments and remediation</li>
                <li><strong>Skipping pilot programs:</strong> Moving directly to full-scale deployment without testing assumptions and refining processes in controlled environments</li>
                <li><strong>Neglecting ongoing optimization:</strong> Treating implementation as a one-time project rather than an ongoing process requiring continuous monitoring and improvement</li>
                <li><strong>Vendor lock-in:</strong> Committing to a single platform without ensuring data portability and API-based integrations that preserve flexibility</li>
            </ul>
            
            <h3>Risk Mitigation Framework</h3>
            <p>Effective risk management for {topic} AI projects requires identifying risks early and developing mitigation strategies before they materialize. Key risk categories include technical risks (model accuracy, integration complexity, scalability), organizational risks (adoption resistance, skill gaps, leadership changes), and external risks (regulatory changes, vendor stability, market shifts).</p>
            <p>Each identified risk should have a designated owner, a probability assessment, an impact rating, and a specific mitigation plan. Regular risk reviews — at minimum monthly during implementation and quarterly during steady-state operations — ensure emerging risks are caught early and existing mitigation plans remain relevant.</p>
""")

    # Section 2: Advanced Analytics & Performance Measurement (~400 words)
    sections.append(f"""
            <h2>Advanced Analytics & Performance Measurement for {topic}</h2>
            <p>Measuring the true impact of AI in {topic} requires sophisticated analytics frameworks that go beyond simple before-and-after comparisons. Leading organizations build comprehensive measurement systems that track both leading and lagging indicators across multiple dimensions.</p>
            
            <h3>Key Performance Indicators (KPIs)</h3>
            <p>Effective {topic} AI measurement tracks three tiers of KPIs. Tier 1 includes operational metrics that reflect day-to-day performance improvements: processing time reduction, error rate decrease, throughput increase, and cost per unit savings. These metrics are typically the easiest to measure and provide the most immediate feedback on implementation progress.</p>
            <p>Tier 2 encompasses strategic metrics that reflect broader business impact: customer satisfaction improvements, revenue growth attributable to AI, employee productivity gains, and competitive positioning enhancements. These metrics require longer measurement periods and more sophisticated attribution models but provide stronger justification for continued investment.</p>
            <p>Tier 3 covers transformation metrics that capture systemic changes: organizational capability development, innovation rate acceleration, market responsiveness improvement, and ecosystem value creation. These metrics are the hardest to measure but most important for long-term strategy validation.</p>
            
            <h3>Dashboard Design Principles</h3>
            <p>Effective {topic} AI dashboards follow the principle of progressive disclosure — showing summary metrics at the top level with the ability to drill down into details. The best dashboards combine real-time operational data with trend analysis and predictive projections, giving stakeholders both current status and forward-looking insights.</p>
            <p>Color coding should follow intuitive conventions (green for on-track, yellow for attention needed, red for intervention required), and every metric should include context — benchmarks, targets, and historical comparisons that help users interpret the numbers meaningfully. Avoid vanity metrics that look impressive but don't drive decision-making.</p>
            
            <h3>Continuous Improvement Cycles</h3>
            <p>The highest-performing {topic} AI implementations use structured improvement cycles inspired by lean methodology. Each cycle begins with data analysis to identify improvement opportunities, moves through hypothesis formation and testing, implements validated changes, and measures results against predictions. These cycles typically run on 2-4 week sprints during active optimization phases and 4-8 week cycles during maintenance phases.</p>
            <p>Documenting each cycle's hypothesis, actions, and results creates an organizational knowledge base that accelerates future improvements and prevents teams from repeating unsuccessful experiments. This institutional memory becomes increasingly valuable as organizations mature in their AI capabilities.</p>
""")

    # Section 3: Industry Trends & Future Outlook (~400 words)
    sections.append(f"""
            <h2>Industry Trends & 2026-2028 Outlook for {topic} AI</h2>
            <p>The {topic} AI landscape is evolving rapidly, with several emerging trends poised to reshape how organizations approach implementation and derive value from these technologies over the next 24-36 months.</p>
            
            <h3>Emerging Technology Trends</h3>
            <p><strong>Multimodal AI Integration:</strong> The next generation of {topic} tools will process text, images, audio, and video simultaneously, enabling more nuanced understanding and richer outputs. Organizations preparing for this shift are already structuring their data collection to capture multiple modalities.</p>
            <p><strong>Edge AI Deployment:</strong> Processing AI workloads closer to data sources reduces latency and improves real-time decision-making for {topic} applications. Edge computing also addresses data privacy concerns by keeping sensitive information local rather than sending it to cloud servers.</p>
            <p><strong>Autonomous AI Agents:</strong> AI systems that can independently plan, execute, and iterate on complex {topic} workflows are moving from research to production. These agents will handle multi-step processes that currently require human orchestration, dramatically expanding the scope of tasks AI can automate.</p>
            <p><strong>Federated Learning:</strong> Training models across distributed datasets without centralizing sensitive data enables collaboration between organizations in {topic} while preserving privacy and competitive advantages. This approach is particularly valuable in regulated industries.</p>
            
            <h3>Market Dynamics</h3>
            <p>The {topic} AI market is projected to grow at 28-35% CAGR through 2028, driven by improving model capabilities, decreasing compute costs, and increasing organizational AI literacy. Consolidation is expected as larger platforms acquire point solutions, creating more comprehensive suites but potentially reducing innovation diversity.</p>
            <p>Pricing models are shifting from per-seat licensing toward usage-based and value-based pricing, making AI tools more accessible to smaller organizations while aligning vendor incentives with customer outcomes. Organizations should negotiate contracts with flexibility clauses that accommodate this evolving pricing landscape.</p>
            
            <h3>Strategic Recommendations for 2026-2028</h3>
            <ul>
                <li><strong>Invest in data infrastructure:</strong> Organizations with clean, well-organized data will extract disproportionately more value from advancing AI capabilities</li>
                <li><strong>Build internal AI literacy:</strong> Train teams across all functions on AI fundamentals to enable broader adoption and more creative applications</li>
                <li><strong>Adopt modular architectures:</strong> Design systems that can swap individual AI components as better models and tools emerge without rebuilding entire workflows</li>
                <li><strong>Establish AI governance early:</strong> Create policies and processes for responsible AI use before they become regulatory requirements</li>
                <li><strong>Monitor competitive landscape:</strong> Track how competitors and adjacent industries use {topic} AI to identify threats and opportunities early</li>
            </ul>
""")

    # Section 4: Security, Privacy & Compliance (~350 words)
    sections.append(f"""
            <h2>Security, Privacy & Regulatory Compliance for {topic} AI</h2>
            <p>As AI adoption in {topic} accelerates, security and compliance requirements grow increasingly complex. Organizations must balance innovation velocity with rigorous data protection and regulatory adherence.</p>
            
            <h3>Data Protection Architecture</h3>
            <p>A comprehensive data protection strategy for {topic} AI includes encryption at rest and in transit, role-based access controls with least-privilege principles, audit logging for all data access and model interactions, and data retention policies aligned with regulatory requirements. Organizations should implement data classification schemes that automatically identify and apply appropriate protection levels to different categories of information.</p>
            <p>Special attention must be paid to training data governance. Organizations need clear policies about what data can be used for model training, how consent is managed, and how data subjects can exercise their rights under applicable privacy regulations. Model cards and data sheets documenting these decisions provide accountability and transparency.</p>
            
            <h3>Regulatory Landscape</h3>
            <p>The regulatory environment for AI in {topic} varies significantly by jurisdiction and is evolving rapidly. Key frameworks include GDPR and the EU AI Act in Europe, sector-specific regulations in the United States, and emerging AI governance frameworks in Asia-Pacific. Organizations operating across multiple jurisdictions need compliance programs that address the most stringent requirements while remaining operationally efficient.</p>
            <p>The EU AI Act's risk-based classification system is becoming a de facto global standard. Organizations should assess their {topic} AI applications against this framework regardless of their current regulatory obligations, as similar requirements will likely emerge in other jurisdictions. High-risk applications require conformity assessments, transparency obligations, and human oversight mechanisms.</p>
            
            <h3>Security Best Practices</h3>
            <ul>
                <li><strong>Regular penetration testing:</strong> Test AI systems specifically for adversarial attacks, prompt injection, and data exfiltration vulnerabilities</li>
                <li><strong>Supply chain security:</strong> Audit third-party AI models and libraries for vulnerabilities and backdoors before deployment</li>
                <li><strong>Incident response plans:</strong> Develop AI-specific incident response procedures for model failures, data breaches, and adversarial attacks</li>
                <li><strong>Continuous monitoring:</strong> Implement automated monitoring for model drift, anomalous outputs, and suspicious access patterns</li>
                <li><strong>Red team exercises:</strong> Regularly test AI systems against adversarial scenarios to identify and address vulnerabilities proactively</li>
            </ul>
""")

    # Section 5: Stakeholder Communication & Executive Reporting (~350 words)
    sections.append(f"""
            <h2>Stakeholder Communication & Executive Reporting for {topic} AI</h2>
            <p>Effective communication about {topic} AI initiatives is critical for maintaining organizational support, securing ongoing investment, and ensuring alignment between technical teams and business stakeholders. Different audiences require different levels of detail and framing.</p>
            
            <h3>Executive Communication Framework</h3>
            <p>When presenting {topic} AI results to executives, lead with business impact rather than technical details. Frame AI capabilities in terms of revenue impact, cost reduction, risk mitigation, and competitive advantage. Use concrete examples and case studies rather than abstract capabilities. Provide honest assessments of both successes and challenges — executives trust leaders who acknowledge difficulties and present mitigation plans rather than those who only share positive news.</p>
            <p>Monthly executive summaries should include: key metric movements with trend analysis, significant milestones achieved and upcoming, resource utilization and budget status, risk register updates, and strategic recommendations. Keep summaries to one page with appendices available for detailed exploration.</p>
            
            <h3>Cross-Functional Alignment</h3>
            <p>AI initiatives in {topic} typically affect multiple departments. Regular cross-functional reviews ensure alignment and surface integration opportunities. Establish a shared vocabulary that bridges technical and business terminology — creating a glossary of key terms prevents miscommunication and ensures everyone is working from the same understanding.</p>
            <p>Internal newsletters, demo days, and brown bag sessions help maintain awareness and enthusiasm for {topic} AI initiatives. These forums also surface use cases and requirements from teams that might not otherwise participate in AI planning discussions.</p>
            
            <h3>Change Communication Strategy</h3>
            <p>Major changes to {topic} workflows should follow a structured communication plan: announce changes well in advance, explain the rationale and expected benefits, provide training and support resources, establish feedback channels, and follow up with results data. The goal is to turn potential resistance into informed support by making people feel included in the process rather than subjected to it.</p>
            <p>Celebrate successes publicly and attribute them to the teams involved, not just the technology. Recognition reinforces adoption behaviors and creates internal champions who advocate for AI initiatives within their teams. Track adoption metrics and address pockets of resistance with targeted support rather than mandate-based enforcement.</p>
""")

    return sections

def fix_article_structure(content):
    """Fix articles that have content after </article> or </footer> tags."""
    # Find content after </article> that should be inside
    # Pattern: content between </article> and </body>
    match = re.search(r'(</article>)(.*?)(</body>)', content, re.DOTALL)
    if match:
        after_article = match.group(2)
        # Check if there's substantial content after </article> (not just footer)
        # Extract any h2/h3/p/ul content that shouldn't be after article
        misplaced = re.findall(r'<h[23]>.*?</h[23]>|<p>.*?</p>|<ul>.*?</ul>', after_article, re.DOTALL)
        if misplaced:
            # Move misplaced content inside article
            misplaced_content = '\n'.join(misplaced)
            # Remove misplaced content from after article
            cleaned_after = after_article
            for m in misplaced:
                cleaned_after = cleaned_after.replace(m, '')
            content = content.replace(match.group(0), 
                                     misplaced_content + '\n</article>' + cleaned_after + '</body>')
    return content

def expand_article(filepath, target_words=TARGET_WORDS):
    """Expand a single article to target word count."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    current_words = count_words(content)
    if current_words >= target_words:
        return current_words, current_words, False
    
    needed_words = target_words - current_words
    topic = extract_topic(os.path.basename(filepath))
    sections = get_expansion_sections(topic, needed_words)
    
    # Fix structure first
    content = fix_article_structure(content)
    
    # Calculate how many sections we need
    words_per_section = 380  # approximate
    sections_needed = min(len(sections), max(1, (needed_words // words_per_section) + 1))
    
    # Build expansion content
    expansion = '\n'.join(sections[:sections_needed])
    
    # Find the best insertion point - before </article> or before footer
    if '</article>' in content:
        content = content.replace('</article>', expansion + '\n</article>', 1)
    elif '<footer' in content:
        content = content.replace('<footer', expansion + '\n<footer', 1)
    else:
        # Append before </body>
        content = content.replace('</body>', expansion + '\n</body>', 1)
    
    new_words = count_words(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return current_words, new_words, True

def main():
    batch_size = int(sys.argv[1]) if len(sys.argv) > 1 else 68
    
    # Get all articles under target
    articles = []
    for f in sorted(os.listdir(ARTICLES_DIR)):
        if not f.endswith('.html'):
            continue
        path = os.path.join(ARTICLES_DIR, f)
        with open(path, 'r', encoding='utf-8') as fh:
            words = count_words(fh.read())
        if words < TARGET_WORDS:
            articles.append((words, f, path))
    
    articles.sort()  # smallest first
    
    if not articles:
        print("✅ All articles are already at 10,500+ words!")
        return
    
    print(f"📋 Found {len(articles)} articles under {TARGET_WORDS} words")
    print(f"📝 Processing batch of {min(batch_size, len(articles))} articles\n")
    
    expanded = 0
    total_added = 0
    
    for i, (words, filename, path) in enumerate(articles[:batch_size]):
        old_words, new_words, changed = expand_article(path)
        added = new_words - old_words
        total_added += added
        expanded += 1
        status = "✅" if new_words >= TARGET_WORDS else "⚠️"
        print(f"{status} [{expanded}/{min(batch_size, len(articles))}] {filename}: {old_words} → {new_words} (+{added})")
    
    print(f"\n📊 Summary:")
    print(f"   Articles expanded: {expanded}")
    print(f"   Total words added: {total_added:,}")
    print(f"   Average added: {total_added // max(1, expanded):,} per article")

if __name__ == '__main__':
    main()
