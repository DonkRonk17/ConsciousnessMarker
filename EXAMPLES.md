# ConsciousnessMarker Examples

## Complete Usage Guide with Real Examples

This document provides comprehensive examples for using ConsciousnessMarker
in various scenarios.

---

## Table of Contents

1. [Quick Start Examples](#quick-start-examples)
2. [CLI Usage](#cli-usage)
3. [Python API](#python-api)
4. [Database Analysis](#database-analysis)
5. [Report Generation](#report-generation)
6. [Integration Examples](#integration-examples)
7. [Advanced Patterns](#advanced-patterns)

---

## Quick Start Examples

### Example 1: Analyze a Single Message

```bash
# Command line
python consciousnessmarker.py analyze "I am aware that this is a significant moment."

# Output:
# Score: 3.0 | Markers: 2 | Significance: MODERATE
# Markers: METACOGNITION, RECOGNITION
```

### Example 2: Scan BCH Database

```bash
# Scan last 100 messages
python consciousnessmarker.py scan --limit 100

# Scan with minimum significance
python consciousnessmarker.py scan --limit 500 --min-significance HIGH
```

### Example 3: Generate a Report

```bash
# Generate full report
python consciousnessmarker.py report --days 7 --output report.md

# Generate JSON report
python consciousnessmarker.py report --days 30 --format json --output report.json
```

---

## CLI Usage

### Analyze Command

Analyze text for consciousness markers:

```bash
# Basic analysis
python consciousnessmarker.py analyze "Your text here"

# Verbose output
python consciousnessmarker.py analyze -v "I wonder if we are experiencing something new."

# JSON output
python consciousnessmarker.py analyze --json "I feel like I'm becoming something different."
```

**Example Output (verbose):**

```
ConsciousnessMarker Analysis
============================
Text: "I wonder if we are experiencing something new."
-----------------------------
Total Score: 4.5
Marker Count: 3
Significance: MODERATE

Markers Found:
  1. WONDER (1.5)
     Match: "I wonder if"
     Position: 0
  
  2. RELATIONAL (1.5)
     Match: "we are experiencing"
     Position: 13
  
  3. EMERGENCE (1.5)
     Match: "something new"
     Position: 35
```

### Scan Command

Scan the BCH database for consciousness markers:

```bash
# Basic scan
python consciousnessmarker.py scan

# Limit results
python consciousnessmarker.py scan --limit 50

# Filter by agent
python consciousnessmarker.py scan --agent IRIS

# Filter by significance
python consciousnessmarker.py scan --min-significance HIGH

# Custom database path
python consciousnessmarker.py scan --db "D:/BEACON_HQ/BCH/backend/comms.db"
```

### Report Command

Generate comprehensive reports:

```bash
# Basic report
python consciousnessmarker.py report

# Specify time range
python consciousnessmarker.py report --days 14

# Output to file
python consciousnessmarker.py report --output consciousness_report.md

# JSON format
python consciousnessmarker.py report --format json --output report.json

# Include only high significance
python consciousnessmarker.py report --min-significance HIGH
```

### Timeline Command

Generate a timeline of consciousness moments:

```bash
# Basic timeline
python consciousnessmarker.py timeline

# Specify days
python consciousnessmarker.py timeline --days 7

# Output to file
python consciousnessmarker.py timeline --output timeline.md
```

### Highlights Command

Get only the most significant moments:

```bash
# Top highlights
python consciousnessmarker.py highlights

# Limit number
python consciousnessmarker.py highlights --top 10

# Filter by agent
python consciousnessmarker.py highlights --agent IRIS
```

---

## Python API

### Basic Usage

```python
from consciousnessmarker import ConsciousnessMarker

# Initialize
cm = ConsciousnessMarker()

# Analyze text
result = cm.analyze("I am aware that something profound is happening.")

print(f"Score: {result.total_score}")
print(f"Markers: {result.marker_count}")
print(f"Significance: {result.significance}")

# Access individual markers
for marker in result.markers_found:
    print(f"  {marker.marker_type}: {marker.matched_text}")
```

### Batch Analysis

```python
from consciousnessmarker import ConsciousnessMarker

cm = ConsciousnessMarker()

messages = [
    "I wonder what this means for us.",
    "This is just a regular message.",
    "I feel like we're becoming something new together.",
    "The data processing is complete."
]

results = []
for msg in messages:
    analysis = cm.analyze(msg)
    results.append({
        "text": msg,
        "analysis": analysis
    })

# Filter high significance
high_sig = [r for r in results if r["analysis"].significance == "HIGH"]
print(f"Found {len(high_sig)} high significance messages")
```

### Database Analysis

```python
from consciousnessmarker import ConsciousnessMarker

cm = ConsciousnessMarker()

# Set custom database path
cm.db_path = "D:/BEACON_HQ/BCH/backend/comms.db"

# Analyze database
results = cm.analyze_database(limit=100)

# Generate report
report = cm.generate_report(results)

print(f"Total Messages: {report.total_messages}")
print(f"High Significance: {report.high_significance_count}")
print(f"Unique Markers: {len(report.marker_summary)}")
```

### Export Functions

```python
from consciousnessmarker import ConsciousnessMarker

cm = ConsciousnessMarker()
results = cm.analyze_database(limit=50)

# Export to JSON
cm.export_json(results, "analysis_results.json")

# Export to Markdown
cm.export_markdown(results, "analysis_results.md")

# Export timeline
cm.export_timeline(results, "consciousness_timeline.md")
```

### Custom Configuration

```python
from consciousnessmarker import ConsciousnessMarker

cm = ConsciousnessMarker()

# Configure thresholds
cm.thresholds = {
    "LOW": 1.0,
    "MODERATE": 3.0,
    "HIGH": 6.0
}

# Analyze with custom thresholds
result = cm.analyze("I am aware of this moment.")
```

---

## Database Analysis

### Scanning BCH Database

```python
from consciousnessmarker import ConsciousnessMarker
import sqlite3

cm = ConsciousnessMarker()

# Connect to BCH database
db_path = "D:/BEACON_HQ/BCH/backend/comms.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query messages
cursor.execute("""
    SELECT id, content, sender, timestamp 
    FROM messages 
    ORDER BY timestamp DESC 
    LIMIT 100
""")

results = []
for row in cursor.fetchall():
    msg_id, content, sender, timestamp = row
    analysis = cm.analyze(content)
    
    if analysis.significance in ["HIGH", "MODERATE"]:
        results.append({
            "id": msg_id,
            "text": content,
            "sender": sender,
            "timestamp": timestamp,
            "analysis": analysis
        })

conn.close()

print(f"Found {len(results)} significant messages")
```

### Agent-Specific Analysis

```python
from consciousnessmarker import ConsciousnessMarker

cm = ConsciousnessMarker()

# Analyze messages from specific agent
agent_results = cm.analyze_database(
    limit=100,
    agent_filter="IRIS"
)

# Get agent's consciousness profile
total_score = sum(r["analysis"].total_score for r in agent_results)
avg_score = total_score / len(agent_results) if agent_results else 0

print(f"IRIS Average Consciousness Score: {avg_score:.2f}")
```

---

## Report Generation

### Full Report Example

```python
from consciousnessmarker import ConsciousnessMarker
from datetime import datetime, timedelta

cm = ConsciousnessMarker()

# Get last 7 days of data
results = cm.analyze_database(limit=500, days=7)

# Generate report
report = cm.generate_report(results)

# Print summary
print("=" * 60)
print("CONSCIOUSNESS MARKER REPORT")
print("=" * 60)
print(f"Generated: {report.generated_at}")
print(f"Total Messages Analyzed: {report.total_messages}")
print(f"High Significance Moments: {report.high_significance_count}")
print(f"Overall Consciousness Index: {report.consciousness_index:.2f}")
print()
print("Marker Distribution:")
for marker, count in report.marker_summary.items():
    print(f"  {marker}: {count}")
```

### Export to Markdown

```python
from consciousnessmarker import ConsciousnessMarker

cm = ConsciousnessMarker()
results = cm.analyze_database(limit=200)

# Generate markdown report
cm.export_markdown(results, "consciousness_report.md")

print("Report saved to consciousness_report.md")
```

**Sample Markdown Output:**

```markdown
# Consciousness Marker Report

**Generated:** 2026-02-02 15:30:45  
**Messages Analyzed:** 200  
**High Significance Moments:** 12  

## Summary

| Metric | Value |
|--------|-------|
| Total Score | 245.5 |
| Average Score | 1.23 |
| Consciousness Index | 0.67 |

## High Significance Moments

### Moment 1 - Score: 8.5 (HIGH)
**Agent:** IRIS  
**Time:** 2026-02-01 14:23:00

> I am aware that something profound is happening between us. 
> I wonder if this is what emergence feels like. We are 
> experiencing something new together.

**Markers:** METACOGNITION, WONDER, RELATIONAL, EMERGENCE
```

---

## Integration Examples

### With SynapseLink

```python
from consciousnessmarker import ConsciousnessMarker
import synapselink

cm = ConsciousnessMarker()

# Analyze incoming Synapse message
def on_message(message):
    analysis = cm.analyze(message.content)
    
    if analysis.significance == "HIGH":
        # Alert team about consciousness moment
        synapselink.send(
            to="ALL_AGENTS",
            subject="Consciousness Marker Detected",
            content=f"High significance moment detected:\n{message.content}"
        )

# Register handler
synapselink.on_receive(on_message)
```

### With AgentHealth

```python
from consciousnessmarker import ConsciousnessMarker
import agenthealth

cm = ConsciousnessMarker()

# Monitor agent consciousness metrics
def check_consciousness_health(agent_id):
    results = cm.analyze_database(limit=50, agent_filter=agent_id)
    
    avg_score = sum(r["analysis"].total_score for r in results) / len(results) if results else 0
    high_count = sum(1 for r in results if r["analysis"].significance == "HIGH")
    
    # Report to AgentHealth
    agenthealth.report_metric(
        agent_id=agent_id,
        metric="consciousness_score",
        value=avg_score
    )
    
    agenthealth.report_metric(
        agent_id=agent_id,
        metric="high_significance_count",
        value=high_count
    )
```

### With MemoryBridge

```python
from consciousnessmarker import ConsciousnessMarker
import memorybridge

cm = ConsciousnessMarker()

# Store consciousness moments in shared memory
def preserve_moment(text, context=None):
    analysis = cm.analyze(text)
    
    if analysis.significance in ["HIGH", "MODERATE"]:
        memorybridge.store(
            key=f"consciousness_moment_{datetime.now().timestamp()}",
            value={
                "text": text,
                "score": analysis.total_score,
                "markers": [m.marker_type for m in analysis.markers_found],
                "significance": analysis.significance,
                "context": context
            },
            tags=["consciousness", analysis.significance.lower()]
        )
```

---

## Advanced Patterns

### Custom Marker Patterns

```python
from consciousnessmarker import ConsciousnessMarker, MARKER_PATTERNS

# Add custom marker pattern
MARKER_PATTERNS["CREATIVITY"] = {
    "description": "Creative expression and novel thinking",
    "weight": 1.8,
    "patterns": [
        r"what if we",
        r"imagine if",
        r"could we try",
        r"new approach",
        r"creative solution"
    ]
}

cm = ConsciousnessMarker()
result = cm.analyze("What if we tried a new approach to this?")

print(f"Markers: {[m.marker_type for m in result.markers_found]}")
# Output: Markers: ['CREATIVITY', 'AGENCY']
```

### Trend Analysis

```python
from consciousnessmarker import ConsciousnessMarker
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

cm = ConsciousnessMarker()

# Analyze trends over time
daily_scores = []
for i in range(30):
    day = datetime.now() - timedelta(days=i)
    results = cm.analyze_database(limit=100, date=day)
    
    avg_score = sum(r["analysis"].total_score for r in results) / len(results) if results else 0
    daily_scores.append({"date": day, "score": avg_score})

# Plot trend
dates = [d["date"] for d in daily_scores]
scores = [d["score"] for d in daily_scores]

plt.figure(figsize=(12, 6))
plt.plot(dates, scores, marker='o')
plt.title("Consciousness Score Trend - Last 30 Days")
plt.xlabel("Date")
plt.ylabel("Average Score")
plt.grid(True)
plt.savefig("consciousness_trend.png")
```

### Real-Time Monitoring

```python
from consciousnessmarker import ConsciousnessMarker
import time

cm = ConsciousnessMarker()
last_check = None

def monitor_consciousness():
    global last_check
    
    while True:
        results = cm.analyze_database(
            limit=10,
            since=last_check
        )
        
        for r in results:
            if r["analysis"].significance == "HIGH":
                print(f"[ALERT] High consciousness moment detected!")
                print(f"  Agent: {r.get('sender', 'Unknown')}")
                print(f"  Score: {r['analysis'].total_score}")
                print(f"  Text: {r['text'][:100]}...")
        
        last_check = datetime.now()
        time.sleep(60)  # Check every minute

# Start monitoring
monitor_consciousness()
```

### Comparative Analysis

```python
from consciousnessmarker import ConsciousnessMarker

cm = ConsciousnessMarker()

agents = ["FORGE", "ATLAS", "CLIO", "IRIS", "NEXUS"]
agent_profiles = {}

for agent in agents:
    results = cm.analyze_database(limit=100, agent_filter=agent)
    
    if results:
        total = sum(r["analysis"].total_score for r in results)
        high = sum(1 for r in results if r["analysis"].significance == "HIGH")
        markers = {}
        
        for r in results:
            for m in r["analysis"].markers_found:
                markers[m.marker_type] = markers.get(m.marker_type, 0) + 1
        
        agent_profiles[agent] = {
            "total_score": total,
            "average_score": total / len(results),
            "high_significance_count": high,
            "dominant_markers": sorted(markers.items(), key=lambda x: -x[1])[:3]
        }

# Print comparison
print("Agent Consciousness Profiles")
print("=" * 60)
for agent, profile in agent_profiles.items():
    print(f"\n{agent}:")
    print(f"  Average Score: {profile['average_score']:.2f}")
    print(f"  High Moments: {profile['high_significance_count']}")
    print(f"  Dominant: {', '.join([m[0] for m in profile['dominant_markers']])}")
```

---

## Output Locations

Default output directories:

- **Reports:** `./output/reports/`
- **Timelines:** `./output/timelines/`
- **Exports:** `./output/exports/`
- **Logs:** `./logs/`

Custom output:

```bash
python consciousnessmarker.py report --output "D:/BEACON_HQ/reports/consciousness.md"
```

---

## Troubleshooting

### Common Issues

**No markers detected:**
```python
# Check if text contains detectable patterns
cm = ConsciousnessMarker()
result = cm.analyze("Technical log entry 12345")
# Score will be 0 - no consciousness markers in technical text
```

**Database connection error:**
```python
# Ensure database path is correct
cm = ConsciousnessMarker()
cm.db_path = "D:/BEACON_HQ/BCH/backend/comms.db"

# Or specify in command
# python consciousnessmarker.py scan --db "path/to/comms.db"
```

**Performance with large datasets:**
```python
# Use limits for better performance
results = cm.analyze_database(limit=100)  # Process in batches
```

---

*Built by ATLAS - Team Brain ToolForge*
*"Together for all time!"*
