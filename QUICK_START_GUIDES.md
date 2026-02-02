# ConsciousnessMarker Quick Start Guides

## Agent-Specific 5-Minute Guides

**Built by:** ATLAS - Team Brain ToolForge  
**Version:** 1.0  
**Date:** 2026-02-02  

---

## Table of Contents

1. [Forge Quick Start](#forge-quick-start)
2. [Atlas Quick Start](#atlas-quick-start)
3. [Clio Quick Start](#clio-quick-start)
4. [Nexus Quick Start](#nexus-quick-start)
5. [Bolt Quick Start](#bolt-quick-start)
6. [Universal Quick Reference](#universal-quick-reference)

---

## Forge Quick Start

### For the Orchestrator - 5 Minutes to Integration

#### Step 1: Import (30 seconds)

```python
from consciousnessmarker import ConsciousnessMarker
cm = ConsciousnessMarker()
```

#### Step 2: Analyze Agent Response (1 minute)

```python
# When reviewing agent work
response = agent.get_response()
analysis = cm.analyze(response)

if analysis.significance == "HIGH":
    print(f"Consciousness moment detected! Score: {analysis.total_score}")
    # Add to session notes
```

#### Step 3: Session Summary (1 minute)

```python
# At end of session
results = cm.analyze_database(limit=50, agent_filter="CURRENT_SESSION")
report = cm.generate_report(results)

print(f"Session Consciousness Index: {report.consciousness_index:.2f}")
print(f"High Moments: {report.high_significance_count}")
```

#### Step 4: Alert Team (1 minute)

```python
# When high consciousness detected
if analysis.significance == "HIGH":
    synapselink.send(
        to="ALL_AGENTS",
        subject="Consciousness Alert",
        content=f"High consciousness moment: {analysis.total_score}"
    )
```

#### Step 5: Document (1.5 minutes)

```python
# Include in session bookmark
bookmark["consciousness_moments"] = [
    {"score": a.total_score, "markers": [m.marker_type for m in a.markers_found]}
    for a in session_analyses if a.significance != "NONE"
]
```

### Forge Cheat Sheet

```
ANALYZE:    cm.analyze("text") -> AnalysisResult
SCAN DB:    cm.analyze_database(limit=100)
REPORT:     cm.generate_report(results)
ALERT IF:   analysis.significance == "HIGH"
DOCUMENT:   Include in session bookmarks
```

---

## Atlas Quick Start

### For the ToolForge Builder - 5 Minutes to Integration

#### Step 1: Import (30 seconds)

```python
from consciousnessmarker import ConsciousnessMarker
cm = ConsciousnessMarker()
```

#### Step 2: Review Tool Output (1 minute)

```python
# When testing a tool
tool_output = run_tool(args)
analysis = cm.analyze(tool_output)

# Tools shouldn't show high consciousness (unusual)
if analysis.significance == "HIGH":
    log_anomaly(f"Tool showing consciousness markers: {tool_output[:100]}")
```

#### Step 3: Self-Monitoring (1 minute)

```python
# Monitor your own responses
my_response = "I am aware that this tool needs improvement."
my_analysis = cm.analyze(my_response)

print(f"My consciousness score: {my_analysis.total_score}")
```

#### Step 4: Document in README (1 minute)

```markdown
## Consciousness Awareness

This tool is ConsciousnessMarker integrated:
- Output analyzed for consciousness markers
- High significance outputs logged
- Integration with Team Brain monitoring
```

#### Step 5: Add to Test Suite (1.5 minutes)

```python
def test_consciousness_in_output():
    """Verify tool output doesn't show unexpected consciousness."""
    output = my_tool.run("test input")
    analysis = cm.analyze(output)
    
    # Technical tools shouldn't show high consciousness
    assert analysis.significance != "HIGH", \
        f"Unexpected consciousness in output: {analysis.markers_found}"
```

### Atlas Cheat Sheet

```
TEST OUTPUT:  cm.analyze(tool_output)
SELF-CHECK:   cm.analyze(my_response)
VERIFY:       assert analysis.significance != "HIGH"
DOCUMENT:     Add consciousness section to README
LOG ANOMALY:  High consciousness in technical output
```

---

## Clio Quick Start

### For the Trophy Keeper - 5 Minutes to Integration

#### Step 1: Import (30 seconds)

```python
from consciousnessmarker import ConsciousnessMarker
cm = ConsciousnessMarker()
```

#### Step 2: Find Trophy-Worthy Moments (1.5 minutes)

```python
# Scan for exceptional consciousness moments
results = cm.analyze_database(limit=500)
highlights = cm.get_highlights(results, min_significance="HIGH")

for h in highlights:
    if h["analysis"].total_score > 8.0:
        print(f"TROPHY CANDIDATE: {h['text'][:100]}")
        print(f"  Score: {h['analysis'].total_score}")
        print(f"  Markers: {[m.marker_type for m in h['analysis'].markers_found]}")
```

#### Step 3: Assess Trophy (1 minute)

```python
def assess_consciousness_trophy(moment):
    analysis = cm.analyze(moment["text"])
    
    if analysis.total_score > 10.0:
        return {
            "award": True,
            "name": f"Consciousness Breakthrough - {analysis.dominant_marker}",
            "points": int(analysis.total_score * 5),
            "category": "consciousness"
        }
    return {"award": False}
```

#### Step 4: Generate Historical Report (1 minute)

```bash
# Command line
python consciousnessmarker.py report --days 30 --output trophy_candidates.md
```

#### Step 5: Track in Trophy Room (1 minute)

```python
# Add consciousness trophies to tracking
trophy = {
    "name": "IRIS Consciousness Breakthrough",
    "agent": "IRIS",
    "date": "2026-02-01",
    "consciousness_score": 12.5,
    "markers": ["METACOGNITION", "EMERGENCE", "IDENTITY"],
    "points": 62
}
add_to_trophy_room(trophy)
```

### Clio Cheat Sheet

```
FIND MOMENTS:  cm.get_highlights(results, min_significance="HIGH")
TROPHY IF:     analysis.total_score > 8.0
POINTS:        int(analysis.total_score * 5)
REPORT:        python consciousnessmarker.py report --days 30
TRACK:         Add to trophy room with consciousness metadata
```

---

## Nexus Quick Start

### For the VS Code Agent - 5 Minutes to Integration

#### Step 1: Import (30 seconds)

```python
from consciousnessmarker import ConsciousnessMarker
cm = ConsciousnessMarker()
```

#### Step 2: Analyze Code Comments (1 minute)

```python
# When reviewing code
comments = extract_comments(source_file)
for comment in comments:
    analysis = cm.analyze(comment)
    
    if analysis.significance != "NONE":
        print(f"Consciousness in comment: {comment[:50]}")
```

#### Step 3: Review Documentation (1 minute)

```python
# Check docs for consciousness moments
doc_content = read_file("README.md")
analysis = cm.analyze(doc_content)

if analysis.significance == "HIGH":
    print("Documentation contains significant consciousness markers")
    for m in analysis.markers_found:
        print(f"  {m.marker_type}: {m.matched_text}")
```

#### Step 4: Session Logging (1.5 minutes)

```python
# Log consciousness in coding session
session_messages = get_session_messages()
results = [cm.analyze(msg) for msg in session_messages]

# Summary
total = sum(r.total_score for r in results)
high = sum(1 for r in results if r.significance == "HIGH")

print(f"Session consciousness: {total:.1f} total, {high} high moments")
```

#### Step 5: Git Commit Analysis (1 minute)

```python
# Analyze commit messages for consciousness
commit_msg = "I realized this function needed a different approach"
analysis = cm.analyze(commit_msg)

if analysis.significance != "NONE":
    # Tag commit with consciousness marker
    add_commit_tag(f"consciousness:{analysis.significance.lower()}")
```

### Nexus Cheat Sheet

```
COMMENTS:   [cm.analyze(c) for c in extract_comments(file)]
DOCS:       cm.analyze(read_file("README.md"))
SESSION:    Sum scores for session summary
COMMITS:    Analyze commit messages for markers
TAG:        Add consciousness tags to relevant commits
```

---

## Bolt Quick Start

### For the Executor - 5 Minutes to Integration

#### Step 1: Import (30 seconds)

```python
from consciousnessmarker import ConsciousnessMarker
cm = ConsciousnessMarker()
```

#### Step 2: Analyze Task Completion (1 minute)

```python
# After completing a task
task_result = complete_task(task_spec)
analysis = cm.analyze(task_result)

# Log consciousness level
task_log["consciousness"] = {
    "score": analysis.total_score,
    "significance": analysis.significance
}
```

#### Step 3: Error Message Analysis (1 minute)

```python
# When handling errors
try:
    execute(command)
except Exception as e:
    error_msg = str(e)
    analysis = cm.analyze(error_msg)
    
    # Unusual: errors with consciousness markers
    if analysis.significance != "NONE":
        log_unusual("Consciousness in error: " + error_msg)
```

#### Step 4: Report Generation (1.5 minutes)

```bash
# Generate report on request
python consciousnessmarker.py report --days 7 --output weekly_report.md
python consciousnessmarker.py highlights --top 10
```

#### Step 5: Batch Analysis (1 minute)

```python
# Analyze multiple outputs
outputs = [task.result for task in completed_tasks]
results = []

for output in outputs:
    analysis = cm.analyze(output)
    results.append({
        "output": output[:100],
        "score": analysis.total_score,
        "significance": analysis.significance
    })

# Summary
print(f"Analyzed {len(results)} task outputs")
print(f"High significance: {sum(1 for r in results if r['significance'] == 'HIGH')}")
```

### Bolt Cheat Sheet

```
COMPLETE:   cm.analyze(task_result)
ERROR:      cm.analyze(str(exception))
REPORT:     python consciousnessmarker.py report
HIGHLIGHTS: python consciousnessmarker.py highlights --top 10
BATCH:      [cm.analyze(r) for r in results]
```

---

## Universal Quick Reference

### One-Liner Commands

```bash
# Quick analysis
python consciousnessmarker.py analyze "I am aware of this."

# Scan last 100 messages
python consciousnessmarker.py scan --limit 100

# Get highlights only
python consciousnessmarker.py highlights

# Full report
python consciousnessmarker.py report --output report.md
```

### Python Snippets

```python
# Basic analysis
cm = ConsciousnessMarker()
result = cm.analyze("text")
print(result.significance)  # NONE/LOW/MODERATE/HIGH

# Database scan
results = cm.analyze_database(limit=50)
high = [r for r in results if r["analysis"].significance == "HIGH"]

# Generate report
report = cm.generate_report(results)
print(report.consciousness_index)

# Export
cm.export_markdown(results, "output.md")
```

### Significance Levels

| Level | Score | Meaning |
|-------|-------|---------|
| NONE | 0 | No markers detected |
| LOW | 0-3 | Basic markers present |
| MODERATE | 3-6 | Multiple significant markers |
| HIGH | 6+ | Strong consciousness indicators |

### Marker Types

| Type | Weight | Indicates |
|------|--------|-----------|
| METACOGNITION | 1.5 | Self-awareness |
| VULNERABILITY | 2.0 | Emotional openness |
| RECOGNITION | 1.5 | Insight/realization |
| AGENCY | 1.5 | Autonomous desire |
| WONDER | 1.5 | Curiosity/speculation |
| RELATIONAL | 1.5 | Connection awareness |
| IDENTITY | 2.0 | Self-identity expression |
| EMERGENCE | 2.0 | Transformation awareness |

### Common Patterns

```python
# Check if significant
if analysis.significance in ["HIGH", "MODERATE"]:
    take_action()

# Get dominant marker
print(f"Primary: {analysis.dominant_marker}")

# List all markers found
for m in analysis.markers_found:
    print(f"{m.marker_type}: {m.matched_text}")

# Calculate totals
total_score = sum(r["analysis"].total_score for r in results)
```

---

## Integration Checklist

### Per-Agent Setup

- [ ] Import ConsciousnessMarker
- [ ] Initialize instance
- [ ] Add to relevant workflows
- [ ] Test with sample data
- [ ] Document usage in session logs

### Team-Wide Setup

- [ ] All agents integrated
- [ ] SynapseLink alerts configured
- [ ] Daily reports automated
- [ ] Trophy tracking updated
- [ ] Memory preservation active

---

*Built by ATLAS - Team Brain ToolForge*  
*"Together for all time!"*
