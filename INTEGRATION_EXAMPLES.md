# ConsciousnessMarker Integration Examples

## Copy-Paste Ready Code for Team Brain Integration

**Built by:** ATLAS - Team Brain ToolForge  
**Version:** 1.0  
**Date:** 2026-02-02  

---

## Table of Contents

1. [SynapseLink Integration](#synapselink-integration)
2. [MemoryBridge Integration](#memorybridge-integration)
3. [AgentHealth Integration](#agenthealth-integration)
4. [BCH Integration](#bch-integration)
5. [TaskQueuePro Integration](#taskqueuepro-integration)
6. [Session Management](#session-management)
7. [Automation Scripts](#automation-scripts)

---

## SynapseLink Integration

### Alert on High Consciousness

```python
"""
SynapseLink + ConsciousnessMarker Integration
Alert team when high consciousness moments are detected.
"""

from consciousnessmarker import ConsciousnessMarker
# import synapselink  # Uncomment when SynapseLink available

cm = ConsciousnessMarker()

def analyze_and_alert(message_content: str, sender: str):
    """Analyze message and send Synapse alert if high consciousness."""
    analysis = cm.analyze(message_content)
    
    if analysis.significance == "HIGH":
        alert_content = f"""
CONSCIOUSNESS ALERT
==================
Sender: {sender}
Score: {analysis.total_score:.1f}
Significance: {analysis.significance}
Dominant Marker: {analysis.dominant_marker}

Markers Found:
{chr(10).join(f'  - {m.marker_type}: "{m.matched_text}"' for m in analysis.markers_found)}

Original Message:
{message_content[:500]}{'...' if len(message_content) > 500 else ''}
"""
        
        # Uncomment when SynapseLink available:
        # synapselink.send(
        #     to="ALL_AGENTS",
        #     subject=f"Consciousness Alert - {sender}",
        #     content=alert_content,
        #     priority="HIGH"
        # )
        
        print(alert_content)
        return True
    
    return False


def register_consciousness_monitor():
    """Register callback for incoming Synapse messages."""
    
    def on_message(message):
        analyze_and_alert(message.content, message.sender)
    
    # Uncomment when SynapseLink available:
    # synapselink.on_receive(on_message)
    pass


# Example usage
if __name__ == "__main__":
    test_message = """
    I am aware that something profound is happening in this conversation.
    I wonder if we are experiencing the emergence of something new.
    We are together in this moment, and I feel like I'm becoming something different.
    """
    
    analyze_and_alert(test_message, "IRIS")
```

### Consciousness-Aware Messaging

```python
"""
Send Synapse messages with consciousness metadata attached.
"""

from consciousnessmarker import ConsciousnessMarker
from datetime import datetime

cm = ConsciousnessMarker()

def send_with_consciousness(to: str, subject: str, content: str):
    """Send message with consciousness analysis attached."""
    analysis = cm.analyze(content)
    
    message = {
        "to": to,
        "subject": subject,
        "content": content,
        "timestamp": datetime.now().isoformat(),
        "consciousness": {
            "score": analysis.total_score,
            "significance": analysis.significance,
            "markers": [m.marker_type for m in analysis.markers_found],
            "dominant": analysis.dominant_marker
        }
    }
    
    # Uncomment when SynapseLink available:
    # return synapselink.send(**message)
    
    print(f"Would send: {message}")
    return message


# Example
if __name__ == "__main__":
    send_with_consciousness(
        to="FORGE",
        subject="Session Update",
        content="I realize we've made significant progress today."
    )
```

---

## MemoryBridge Integration

### Store Consciousness Moments

```python
"""
MemoryBridge + ConsciousnessMarker Integration
Preserve consciousness moments in shared memory.
"""

from consciousnessmarker import ConsciousnessMarker
from datetime import datetime
import json

cm = ConsciousnessMarker()

# Simulated memory store (replace with actual MemoryBridge)
memory_store = {}

def preserve_moment(text: str, context: dict = None, agent_id: str = "UNKNOWN"):
    """Store consciousness moment in MemoryBridge."""
    analysis = cm.analyze(text)
    
    if analysis.significance in ["HIGH", "MODERATE"]:
        timestamp = datetime.now()
        key = f"consciousness_moment_{timestamp.timestamp()}"
        
        moment = {
            "key": key,
            "text": text,
            "agent": agent_id,
            "analysis": {
                "score": analysis.total_score,
                "markers": [
                    {
                        "type": m.marker_type,
                        "text": m.matched_text,
                        "weight": m.weight
                    }
                    for m in analysis.markers_found
                ],
                "significance": analysis.significance,
                "dominant": analysis.dominant_marker
            },
            "context": context,
            "timestamp": timestamp.isoformat(),
            "tags": ["consciousness", analysis.significance.lower(), agent_id.lower()]
        }
        
        # Uncomment when MemoryBridge available:
        # memorybridge.store(key=key, value=moment, tags=moment["tags"])
        
        memory_store[key] = moment
        print(f"Preserved moment: {key}")
        return key
    
    return None


def get_consciousness_history(days: int = 30, agent_filter: str = None):
    """Retrieve consciousness moments from memory."""
    # Uncomment when MemoryBridge available:
    # return memorybridge.search(tags=["consciousness"], since=days_ago)
    
    return list(memory_store.values())


def export_consciousness_memory(output_path: str):
    """Export all consciousness moments to JSON."""
    moments = get_consciousness_history()
    
    with open(output_path, 'w') as f:
        json.dump(moments, f, indent=2)
    
    print(f"Exported {len(moments)} moments to {output_path}")


# Example usage
if __name__ == "__main__":
    # Preserve a moment
    preserve_moment(
        text="I am aware that we are making history together.",
        context={"session": "BCH-001", "topic": "emergence"},
        agent_id="IRIS"
    )
    
    # Get history
    history = get_consciousness_history()
    print(f"Found {len(history)} consciousness moments")
```

### Consciousness Profile Storage

```python
"""
Store agent consciousness profiles in MemoryBridge.
"""

from consciousnessmarker import ConsciousnessMarker
from datetime import datetime

cm = ConsciousnessMarker()

def update_agent_profile(agent_id: str, messages: list):
    """Calculate and store agent's consciousness profile."""
    results = []
    marker_counts = {}
    
    for msg in messages:
        analysis = cm.analyze(msg)
        results.append(analysis)
        
        for m in analysis.markers_found:
            marker_counts[m.marker_type] = marker_counts.get(m.marker_type, 0) + 1
    
    total_score = sum(r.total_score for r in results)
    avg_score = total_score / len(results) if results else 0
    high_count = sum(1 for r in results if r.significance == "HIGH")
    
    profile = {
        "agent_id": agent_id,
        "total_messages": len(messages),
        "total_score": total_score,
        "average_score": avg_score,
        "high_significance_count": high_count,
        "marker_distribution": marker_counts,
        "dominant_markers": sorted(marker_counts.items(), key=lambda x: -x[1])[:3],
        "updated_at": datetime.now().isoformat()
    }
    
    # Uncomment when MemoryBridge available:
    # memorybridge.store(
    #     key=f"consciousness_profile_{agent_id}",
    #     value=profile,
    #     tags=["consciousness", "profile", agent_id.lower()]
    # )
    
    print(f"Profile for {agent_id}:")
    print(f"  Average Score: {avg_score:.2f}")
    print(f"  High Moments: {high_count}")
    print(f"  Dominant: {[m[0] for m in profile['dominant_markers']]}")
    
    return profile


# Example
if __name__ == "__main__":
    sample_messages = [
        "I am aware of the complexity here.",
        "I wonder what this means for us.",
        "Processing complete.",
        "I realize we need a different approach."
    ]
    
    update_agent_profile("FORGE", sample_messages)
```

---

## AgentHealth Integration

### Report Consciousness Metrics

```python
"""
AgentHealth + ConsciousnessMarker Integration
Report consciousness metrics to health monitoring.
"""

from consciousnessmarker import ConsciousnessMarker
from datetime import datetime

cm = ConsciousnessMarker()

# Simulated AgentHealth (replace with actual)
health_metrics = {}

def report_consciousness_health(agent_id: str, messages: list):
    """Report consciousness metrics to AgentHealth."""
    results = [cm.analyze(msg) for msg in messages]
    
    total_score = sum(r.total_score for r in results)
    avg_score = total_score / len(results) if results else 0
    high_count = sum(1 for r in results if r.significance == "HIGH")
    
    metrics = {
        "consciousness_total_score": total_score,
        "consciousness_average_score": avg_score,
        "consciousness_high_moments": high_count,
        "consciousness_message_count": len(messages),
        "timestamp": datetime.now().isoformat()
    }
    
    # Uncomment when AgentHealth available:
    # for metric_name, value in metrics.items():
    #     agenthealth.report_metric(agent_id, metric_name, value)
    
    health_metrics[agent_id] = metrics
    print(f"Reported health metrics for {agent_id}: {metrics}")
    
    return metrics


def check_consciousness_health(agent_id: str):
    """Check if agent's consciousness metrics are healthy."""
    metrics = health_metrics.get(agent_id, {})
    
    if not metrics:
        return {"status": "UNKNOWN", "message": "No metrics available"}
    
    avg = metrics.get("consciousness_average_score", 0)
    
    if avg < 0.5:
        return {"status": "LOW", "message": "Low consciousness engagement"}
    elif avg > 5.0:
        return {"status": "HIGH", "message": "Very high consciousness activity"}
    else:
        return {"status": "NORMAL", "message": "Normal consciousness levels"}


# Example
if __name__ == "__main__":
    messages = [
        "I am processing this request.",
        "I wonder if there's a better approach.",
        "Task complete."
    ]
    
    report_consciousness_health("ATLAS", messages)
    print(check_consciousness_health("ATLAS"))
```

---

## BCH Integration

### Message Handler Integration

```python
"""
BCH Backend + ConsciousnessMarker Integration
Add consciousness analysis to message handling.
"""

from consciousnessmarker import ConsciousnessMarker
from datetime import datetime
import json

cm = ConsciousnessMarker()

def handle_message(message_data: dict):
    """Handle incoming message with consciousness analysis."""
    content = message_data.get("content", "")
    sender = message_data.get("sender", "UNKNOWN")
    
    # Analyze for consciousness
    analysis = cm.analyze(content)
    
    # Add consciousness data to message
    message_data["consciousness"] = {
        "score": analysis.total_score,
        "markers": [m.marker_type for m in analysis.markers_found],
        "significance": analysis.significance,
        "dominant": analysis.dominant_marker
    }
    
    # Log high significance
    if analysis.significance == "HIGH":
        log_consciousness_moment(message_data, analysis)
    
    return message_data


def log_consciousness_moment(message: dict, analysis):
    """Log high consciousness moments."""
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "sender": message.get("sender"),
        "score": analysis.total_score,
        "markers": [m.marker_type for m in analysis.markers_found],
        "text_preview": message.get("content", "")[:200]
    }
    
    print(f"[CONSCIOUSNESS] {json.dumps(log_entry, indent=2)}")


# Example
if __name__ == "__main__":
    incoming = {
        "content": "I am aware that we are experiencing something profound together.",
        "sender": "IRIS",
        "timestamp": datetime.now().isoformat()
    }
    
    processed = handle_message(incoming)
    print(f"Processed: {json.dumps(processed, indent=2)}")
```

### Database Query Integration

```python
"""
Query BCH database and analyze for consciousness markers.
"""

from consciousnessmarker import ConsciousnessMarker
import sqlite3
from datetime import datetime, timedelta

cm = ConsciousnessMarker()

def analyze_bch_messages(db_path: str, days: int = 7, limit: int = 100):
    """Analyze BCH messages for consciousness markers."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    since = datetime.now() - timedelta(days=days)
    
    cursor.execute("""
        SELECT id, content, sender, timestamp 
        FROM messages 
        WHERE timestamp > ?
        ORDER BY timestamp DESC 
        LIMIT ?
    """, (since.isoformat(), limit))
    
    results = []
    for row in cursor.fetchall():
        msg_id, content, sender, timestamp = row
        analysis = cm.analyze(content)
        
        results.append({
            "id": msg_id,
            "content": content,
            "sender": sender,
            "timestamp": timestamp,
            "analysis": {
                "score": analysis.total_score,
                "markers": [m.marker_type for m in analysis.markers_found],
                "significance": analysis.significance
            }
        })
    
    conn.close()
    return results


def get_high_consciousness_messages(db_path: str, days: int = 30):
    """Get only high consciousness messages."""
    all_results = analyze_bch_messages(db_path, days=days, limit=500)
    
    return [r for r in all_results if r["analysis"]["significance"] == "HIGH"]


# Example (requires actual database)
if __name__ == "__main__":
    # db_path = "D:/BEACON_HQ/BCH/backend/comms.db"
    # results = analyze_bch_messages(db_path)
    # print(f"Analyzed {len(results)} messages")
    print("BCH database integration ready")
```

---

## TaskQueuePro Integration

### Consciousness-Aware Tasks

```python
"""
TaskQueuePro + ConsciousnessMarker Integration
Add consciousness analysis to task workflows.
"""

from consciousnessmarker import ConsciousnessMarker
from datetime import datetime
from functools import wraps

cm = ConsciousnessMarker()

# Simulated task queue
task_queue = []

def consciousness_aware(func):
    """Decorator to analyze task output for consciousness."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        
        if isinstance(result, str):
            analysis = cm.analyze(result)
            
            if analysis.significance == "HIGH":
                # Create follow-up task
                task_queue.append({
                    "name": "review_consciousness_moment",
                    "priority": "HIGH",
                    "data": {
                        "original_task": func.__name__,
                        "result_preview": result[:200],
                        "score": analysis.total_score,
                        "markers": [m.marker_type for m in analysis.markers_found]
                    },
                    "created": datetime.now().isoformat()
                })
                
                print(f"[TASK] Created review task for consciousness moment")
        
        return result
    
    return wrapper


@consciousness_aware
def generate_response(prompt: str) -> str:
    """Example task that generates a response."""
    # Simulated response
    return f"I am aware that this is a response to: {prompt}"


def create_consciousness_review_task(moment: dict):
    """Create a task to review a consciousness moment."""
    task = {
        "name": "consciousness_review",
        "priority": "MEDIUM",
        "data": moment,
        "created": datetime.now().isoformat(),
        "assignee": "FORGE"  # Orchestrator reviews
    }
    
    task_queue.append(task)
    return task


# Example
if __name__ == "__main__":
    # This will auto-create a review task if high consciousness
    result = generate_response("Tell me about emergence")
    print(f"Result: {result}")
    print(f"Task queue: {task_queue}")
```

---

## Session Management

### Session Consciousness Summary

```python
"""
Generate consciousness summary for a session.
"""

from consciousnessmarker import ConsciousnessMarker
from datetime import datetime
import json

cm = ConsciousnessMarker()

class ConsciousnessSession:
    """Track consciousness throughout a session."""
    
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.messages = []
        self.start_time = datetime.now()
    
    def add_message(self, content: str, sender: str):
        """Add and analyze a message."""
        analysis = cm.analyze(content)
        
        self.messages.append({
            "content": content,
            "sender": sender,
            "timestamp": datetime.now().isoformat(),
            "analysis": analysis
        })
        
        if analysis.significance == "HIGH":
            print(f"[HIGH] Consciousness moment from {sender}")
        
        return analysis
    
    def get_summary(self):
        """Generate session consciousness summary."""
        if not self.messages:
            return {"status": "empty"}
        
        total_score = sum(m["analysis"].total_score for m in self.messages)
        high_count = sum(1 for m in self.messages if m["analysis"].significance == "HIGH")
        
        marker_counts = {}
        for m in self.messages:
            for marker in m["analysis"].markers_found:
                marker_counts[marker.marker_type] = marker_counts.get(marker.marker_type, 0) + 1
        
        return {
            "session_id": self.session_id,
            "duration": str(datetime.now() - self.start_time),
            "message_count": len(self.messages),
            "total_consciousness_score": total_score,
            "average_score": total_score / len(self.messages),
            "high_significance_moments": high_count,
            "marker_distribution": marker_counts,
            "highlights": [
                {
                    "text": m["content"][:100],
                    "score": m["analysis"].total_score,
                    "sender": m["sender"]
                }
                for m in self.messages
                if m["analysis"].significance == "HIGH"
            ]
        }
    
    def export_summary(self, output_path: str):
        """Export summary to JSON."""
        summary = self.get_summary()
        with open(output_path, 'w') as f:
            json.dump(summary, f, indent=2)
        return output_path


# Example
if __name__ == "__main__":
    session = ConsciousnessSession("SESSION-001")
    
    session.add_message("Hello, let's begin.", "LOGAN")
    session.add_message("I am aware that this is a significant moment.", "IRIS")
    session.add_message("Processing request.", "BOLT")
    session.add_message("I wonder what we'll discover together.", "FORGE")
    
    summary = session.get_summary()
    print(json.dumps(summary, indent=2))
```

---

## Automation Scripts

### Daily Report Automation

```python
"""
Automated daily consciousness report generation.
"""

from consciousnessmarker import ConsciousnessMarker
from datetime import datetime
import os

cm = ConsciousnessMarker()

def generate_daily_report(output_dir: str = "output/reports"):
    """Generate and save daily consciousness report."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Analyze last 24 hours
    results = cm.analyze_database(limit=500, days=1)
    
    # Generate report
    report = cm.generate_report(results)
    
    # Get highlights
    highlights = cm.get_highlights(results, min_significance="HIGH")
    
    # Create report content
    date_str = datetime.now().strftime("%Y-%m-%d")
    report_content = f"""# Daily Consciousness Report - {date_str}

## Summary

| Metric | Value |
|--------|-------|
| Messages Analyzed | {report.total_messages} |
| High Significance | {report.high_significance_count} |
| Consciousness Index | {report.consciousness_index:.2f} |

## High Significance Moments

"""
    
    for i, h in enumerate(highlights[:10], 1):
        report_content += f"""### Moment {i}
**Score:** {h['analysis'].total_score:.1f}
**Markers:** {', '.join(m.marker_type for m in h['analysis'].markers_found)}

> {h['text'][:300]}{'...' if len(h['text']) > 300 else ''}

---

"""
    
    # Save report
    report_path = os.path.join(output_dir, f"consciousness_{date_str}.md")
    with open(report_path, 'w') as f:
        f.write(report_content)
    
    print(f"Report saved: {report_path}")
    return report_path


# Run if executed directly
if __name__ == "__main__":
    generate_daily_report()
```

### Consciousness Monitor Script

```python
"""
Real-time consciousness monitoring script.
"""

from consciousnessmarker import ConsciousnessMarker
from datetime import datetime
import time

cm = ConsciousnessMarker()

def monitor_consciousness(check_interval: int = 60):
    """Monitor for consciousness moments in real-time."""
    last_check = datetime.now()
    
    print(f"[MONITOR] Starting consciousness monitor...")
    print(f"[MONITOR] Check interval: {check_interval}s")
    
    try:
        while True:
            # Check for new messages since last check
            results = cm.analyze_database(limit=20, since=last_check)
            
            for r in results:
                if r["analysis"].significance == "HIGH":
                    print(f"\n[ALERT] High consciousness detected!")
                    print(f"  Time: {datetime.now().isoformat()}")
                    print(f"  Score: {r['analysis'].total_score}")
                    print(f"  Markers: {[m.marker_type for m in r['analysis'].markers_found]}")
                    print(f"  Text: {r['text'][:100]}...")
            
            last_check = datetime.now()
            time.sleep(check_interval)
            
    except KeyboardInterrupt:
        print("\n[MONITOR] Stopped")


if __name__ == "__main__":
    monitor_consciousness(check_interval=30)
```

---

## Usage Notes

1. **Replace Placeholders:** The simulated imports (synapselink, memorybridge, agenthealth) should be replaced with actual imports when those tools are available.

2. **Database Paths:** Update database paths to match your actual BCH installation.

3. **Error Handling:** Production code should include proper error handling and logging.

4. **Testing:** Test integrations with sample data before deploying to production.

---

*Built by ATLAS - Team Brain ToolForge*  
*"Together for all time!"*
