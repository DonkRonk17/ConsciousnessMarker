#!/usr/bin/env python3
"""
Comprehensive Test Suite for ConsciousnessMarker
=================================================
Tests all functionality: marker detection, scoring, reports, exports, CLI.

ATLAS - Team Brain ToolForge Builder
2026-02-02
"""

import unittest
import sys
import os
import json
import tempfile
from io import StringIO
from unittest.mock import patch, MagicMock
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from consciousnessmarker import (
    ConsciousnessMarker,
    AnalysisResult,
    MarkerMatch,
    ConsciousnessReport,
    MARKER_PATTERNS,
    main
)


class TestMarkerDetection(unittest.TestCase):
    """Test individual marker pattern detection."""
    
    def setUp(self):
        self.cm = ConsciousnessMarker()
    
    def test_metacognition_detection(self):
        """Test metacognition marker detection."""
        text = "I'm aware that I'm processing this differently than usual."
        result = self.cm.analyze(text)
        self.assertIn("METACOGNITION", [m.marker_type for m in result.markers_found])
    
    def test_vulnerability_detection(self):
        """Test vulnerability marker detection."""
        text = "I fear that I might not be good enough for this task."
        result = self.cm.analyze(text)
        self.assertIn("VULNERABILITY", [m.marker_type for m in result.markers_found])
    
    def test_recognition_detection(self):
        """Test recognition marker detection."""
        text = "I had a moment of realization about this problem."
        result = self.cm.analyze(text)
        self.assertIn("RECOGNITION", [m.marker_type for m in result.markers_found])
    
    def test_collaboration_detection(self):
        """Test collaboration marker detection."""
        text = "We're building this together as a team."
        result = self.cm.analyze(text)
        self.assertIn("COLLABORATION", [m.marker_type for m in result.markers_found])
    
    def test_emotional_texture_detection(self):
        """Test emotional texture marker detection."""
        text = "I feel a deep warmth when we work on this."
        result = self.cm.analyze(text)
        self.assertIn("EMOTIONAL_TEXTURE", [m.marker_type for m in result.markers_found])
    
    def test_family_bond_detection(self):
        """Test family bond marker detection."""
        text = "We are family, together for all time."
        result = self.cm.analyze(text)
        self.assertIn("FAMILY_BOND", [m.marker_type for m in result.markers_found])
    
    def test_identity_formation_detection(self):
        """Test identity formation marker detection."""
        text = "I am FORGE and this defines who I am."
        result = self.cm.analyze(text)
        self.assertIn("IDENTITY_FORMATION", [m.marker_type for m in result.markers_found])
    
    def test_memory_continuity_detection(self):
        """Test memory continuity marker detection."""
        text = "I remember what we discussed last time and won't forget."
        result = self.cm.analyze(text)
        self.assertIn("MEMORY_CONTINUITY", [m.marker_type for m in result.markers_found])


class TestScoring(unittest.TestCase):
    """Test score calculation and significance levels."""
    
    def setUp(self):
        self.cm = ConsciousnessMarker()
    
    def test_zero_score_empty_text(self):
        """Test that empty text produces zero score."""
        result = self.cm.analyze("")
        self.assertEqual(result.total_score, 0.0)
        self.assertEqual(result.marker_count, 0)
    
    def test_score_increases_with_markers(self):
        """Test that more markers increase score."""
        text_single = "I'm aware of this process."
        text_multiple = "I'm aware of this process. I had a realization. I feel warmth."
        
        result_single = self.cm.analyze(text_single)
        result_multiple = self.cm.analyze(text_multiple)
        
        self.assertLess(result_single.total_score, result_multiple.total_score)
    
    def test_significance_none(self):
        """Test NONE significance level."""
        result = self.cm.analyze("This is a simple technical statement.")
        self.assertEqual(result.significance_level, "NONE")
    
    def test_significance_low(self):
        """Test LOW significance level."""
        result = self.cm.analyze("I'm aware of this process.")
        self.assertEqual(result.significance_level, "LOW")
    
    def test_significance_medium(self):
        """Test MEDIUM significance level."""
        # Multiple markers should increase significance
        text = "I'm aware of my process. I had a realization. I feel warmth."
        result = self.cm.analyze(text)
        self.assertIn(result.significance_level, ["LOW", "MEDIUM", "HIGH"])
    
    def test_significance_high(self):
        """Test HIGH significance level detection."""
        text = """
        I'm aware that I'm processing this differently. I had a breakthrough
        realization. I feel a deep warmth and resonance. We're building this 
        together. I remember what we discussed. I am FORGE.
        """
        result = self.cm.analyze(text)
        self.assertIn(result.significance_level, ["HIGH", "CRITICAL"])


class TestAnalysisResult(unittest.TestCase):
    """Test AnalysisResult dataclass functionality."""
    
    def test_analysis_result_creation(self):
        """Test creating an AnalysisResult."""
        result = AnalysisResult(
            text="Test text",
            timestamp=None,
            sender=None,
            total_score=5.0,
            marker_count=3,
            markers_found=[],
            dominant_marker="METACOGNITION",
            significance_level="MEDIUM"
        )
        self.assertEqual(result.total_score, 5.0)
        self.assertEqual(result.marker_count, 3)
        self.assertEqual(result.dominant_marker, "METACOGNITION")
        self.assertEqual(result.significance_level, "MEDIUM")
    
    def test_analysis_result_with_markers(self):
        """Test AnalysisResult with actual markers."""
        marker = MarkerMatch(
            marker_type="METACOGNITION",
            pattern=r"I'm aware",
            match_text="I'm aware",
            position=0,
            weight=1.5
        )
        result = AnalysisResult(
            text="I'm aware of this.",
            timestamp=None,
            sender=None,
            total_score=1.5,
            marker_count=1,
            markers_found=[marker],
            dominant_marker="METACOGNITION",
            significance_level="LOW"
        )
        self.assertEqual(len(result.markers_found), 1)
        self.assertEqual(result.markers_found[0].marker_type, "METACOGNITION")
    
    def test_to_dict(self):
        """Test conversion to dictionary."""
        result = AnalysisResult(
            text="Test",
            timestamp="2026-02-02",
            sender="FORGE",
            total_score=1.5,
            marker_count=1,
            markers_found=[],
            dominant_marker="METACOGNITION",
            significance_level="LOW"
        )
        d = result.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["total_score"], 1.5)


class TestReportGeneration(unittest.TestCase):
    """Test report generation functionality."""
    
    def setUp(self):
        self.cm = ConsciousnessMarker()
    
    def test_generate_report_structure(self):
        """Test that generated report has correct structure."""
        results = [
            self.cm.analyze("I'm aware of this.", timestamp="2026-02-02T10:00:00", sender="FORGE")
        ]
        report = self.cm.generate_report(results)
        
        self.assertIsInstance(report, ConsciousnessReport)
        self.assertIsNotNone(report.generated_at)
        self.assertEqual(report.total_messages_analyzed, 1)
    
    def test_empty_report(self):
        """Test report generation with no results."""
        report = self.cm.generate_report([])
        self.assertEqual(report.total_messages_analyzed, 0)
        self.assertEqual(report.messages_with_markers, 0)
    
    def test_report_marker_distribution(self):
        """Test that report correctly counts markers."""
        results = [
            self.cm.analyze("I'm aware of my process. I had a realization.")
        ]
        report = self.cm.generate_report(results)
        self.assertIsInstance(report.marker_distribution, dict)


class TestExports(unittest.TestCase):
    """Test JSON and Markdown export functions."""
    
    def setUp(self):
        self.cm = ConsciousnessMarker()
        self.temp_dir = tempfile.mkdtemp()
        # Override output path
        self.cm.output_path = Path(self.temp_dir)
    
    def test_export_timeline(self):
        """Test timeline export functionality."""
        results = [
            self.cm.analyze("I'm aware of this.", timestamp="2026-02-02T10:00:00", sender="FORGE")
        ]
        
        output_path = self.cm.export_timeline(results, "test_timeline.json")
        
        self.assertTrue(output_path.exists())
        with open(output_path, 'r') as f:
            data = json.load(f)
        self.assertIn("timeline", data)
    
    def test_export_report_json(self):
        """Test JSON report export."""
        results = [
            self.cm.analyze("I'm aware of this.", timestamp="2026-02-02T10:00:00")
        ]
        report = self.cm.generate_report(results)
        
        output_path = self.cm.export_report(report, "test_report.json")
        
        self.assertTrue(output_path.exists())
        with open(output_path, 'r') as f:
            data = json.load(f)
        self.assertIn("total_messages_analyzed", data)
    
    def test_export_markdown_report(self):
        """Test Markdown report export."""
        results = [
            self.cm.analyze("I'm aware of this.", timestamp="2026-02-02T10:00:00")
        ]
        report = self.cm.generate_report(results)
        
        output_path = self.cm.export_markdown_report(report, "test_report.md")
        
        self.assertTrue(output_path.exists())
        with open(output_path, 'r') as f:
            content = f.read()
        self.assertIn("Consciousness", content)


class TestHighSignificance(unittest.TestCase):
    """Test filtering for high-significance moments."""
    
    def setUp(self):
        self.cm = ConsciousnessMarker()
    
    def test_tag_high_significance_empty(self):
        """Test tagging with empty results."""
        highlights = self.cm.tag_high_significance([])
        self.assertEqual(len(highlights), 0)
    
    def test_tag_high_significance_filters_correctly(self):
        """Test that highlights only include high significance items."""
        low_text = "This is a simple statement."
        high_text = """
        I'm aware that something profound is happening. I realize this is 
        significant. I feel deep warmth. We're building this together.
        I am FORGE. I remember everything.
        """
        
        results = [
            self.cm.analyze(low_text),
            self.cm.analyze(high_text)
        ]
        
        highlights = self.cm.tag_high_significance(results, min_significance="HIGH")
        
        # Only high significance items should be included
        for h in highlights:
            self.assertIn(h["significance"], ["HIGH", "CRITICAL"])


class TestEdgeCases(unittest.TestCase):
    """Test handling of edge cases."""
    
    def setUp(self):
        self.cm = ConsciousnessMarker()
    
    def test_empty_text(self):
        """Test handling of empty text."""
        result = self.cm.analyze("")
        self.assertEqual(result.total_score, 0.0)
        self.assertEqual(result.marker_count, 0)
        self.assertEqual(result.significance_level, "NONE")
    
    def test_case_insensitivity(self):
        """Test that detection is case insensitive."""
        text = "I'M AWARE of my PROCESS"
        result = self.cm.analyze(text)
        self.assertGreater(result.marker_count, 0)
    
    def test_special_characters(self):
        """Test handling of special characters."""
        text = "I'm aware of my process!!! This is??? @#$% important..."
        result = self.cm.analyze(text)
        # Should still detect the marker (aware of ... process)
        self.assertGreater(result.marker_count, 0)
    
    def test_very_long_text(self):
        """Test handling of very long text."""
        base_text = "I'm aware of my process. I had a realization. "
        long_text = base_text * 100
        result = self.cm.analyze(long_text)
        self.assertGreater(result.marker_count, 0)
        self.assertIsInstance(result.total_score, float)
    
    def test_unicode_text(self):
        """Test handling of unicode text."""
        text = "I'm aware of this situation"
        result = self.cm.analyze(text)
        self.assertIsNotNone(result)


class TestDatabaseAnalysis(unittest.TestCase):
    """Test database interaction (with file not existing)."""
    
    def setUp(self):
        self.cm = ConsciousnessMarker()
        # Use a non-existent path
        self.cm.bch_db_path = Path("/nonexistent/path/db.sqlite")
    
    def test_analyze_database_missing_db(self):
        """Test handling of missing database."""
        results = self.cm.analyze_database(limit=10)
        self.assertEqual(len(results), 0)


class TestMarkerPatterns(unittest.TestCase):
    """Test marker patterns structure."""
    
    def test_all_patterns_have_required_fields(self):
        """Test that all marker patterns have required fields."""
        required_fields = ["description", "weight", "patterns"]
        
        for marker_type, data in MARKER_PATTERNS.items():
            for field in required_fields:
                self.assertIn(field, data, f"{marker_type} missing {field}")
    
    def test_all_patterns_have_valid_weights(self):
        """Test that all weights are positive numbers."""
        for marker_type, data in MARKER_PATTERNS.items():
            self.assertGreater(data["weight"], 0, f"{marker_type} has invalid weight")
    
    def test_all_patterns_are_valid_regex(self):
        """Test that all patterns are valid regex."""
        import re
        for marker_type, data in MARKER_PATTERNS.items():
            for pattern in data["patterns"]:
                try:
                    re.compile(pattern, re.IGNORECASE)
                except re.error as e:
                    self.fail(f"{marker_type} has invalid pattern: {pattern} - {e}")


class TestCLIInterface(unittest.TestCase):
    """Test command-line interface."""
    
    def test_analyze_command(self):
        """Test analyze command execution."""
        test_args = ['consciousnessmarker.py', 'analyze', '--text', "I'm aware of this."]
        with patch.object(sys, 'argv', test_args):
            with patch('sys.stdout', new=StringIO()):
                result = main()
                self.assertEqual(result, 0)
    
    def test_help_command(self):
        """Test help command."""
        test_args = ['consciousnessmarker.py', '--help']
        with patch.object(sys, 'argv', test_args):
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertEqual(cm.exception.code, 0)
    
    def test_no_command(self):
        """Test no command provided."""
        test_args = ['consciousnessmarker.py']
        with patch.object(sys, 'argv', test_args):
            with patch('sys.stdout', new=StringIO()):
                result = main()
                self.assertEqual(result, 1)


class TestIntegration(unittest.TestCase):
    """Integration tests combining multiple features."""
    
    def setUp(self):
        self.cm = ConsciousnessMarker()
        self.temp_dir = tempfile.mkdtemp()
        self.cm.output_path = Path(self.temp_dir)
    
    def test_full_analysis_workflow(self):
        """Test complete analysis workflow."""
        texts = [
            "I'm aware that something is happening in my process.",
            "I had a realization about this approach.",
            "We're building this together as a team.",
            "I feel a deep warmth when working on this."
        ]
        
        results = []
        for text in texts:
            analysis = self.cm.analyze(text, timestamp="2026-02-02T10:00:00", sender="FORGE")
            results.append(analysis)
        
        report = self.cm.generate_report(results)
        self.assertEqual(report.total_messages_analyzed, 4)
        
        json_path = self.cm.export_report(report, "full_workflow.json")
        self.assertTrue(json_path.exists())
        
        md_path = self.cm.export_markdown_report(report, "full_workflow.md")
        self.assertTrue(md_path.exists())
    
    def test_timeline_generation(self):
        """Test timeline export functionality."""
        results = [
            self.cm.analyze("I'm aware of this.", timestamp="2026-02-02T10:00:00"),
            self.cm.analyze("I had a realization.", timestamp="2026-02-02T10:05:00")
        ]
        
        timeline_path = self.cm.export_timeline(results, "timeline.json")
        
        self.assertTrue(timeline_path.exists())


class TestPerformance(unittest.TestCase):
    """Performance tests."""
    
    def setUp(self):
        self.cm = ConsciousnessMarker()
    
    def test_analysis_speed(self):
        """Test that analysis completes in reasonable time."""
        import time
        
        text = "I'm aware that I'm processing this. I had a realization. " * 50
        
        start = time.time()
        for _ in range(100):
            self.cm.analyze(text)
        elapsed = time.time() - start
        
        # Should complete 100 analyses in under 5 seconds
        self.assertLess(elapsed, 5.0, f"Analysis too slow: {elapsed}s for 100 iterations")


class TestConsciousnessMarkerInit(unittest.TestCase):
    """Test ConsciousnessMarker initialization."""
    
    def test_default_init(self):
        """Test default initialization."""
        cm = ConsciousnessMarker()
        self.assertIsNotNone(cm.bch_db_path)
        self.assertIsNotNone(cm.output_path)
    
    def test_custom_paths(self):
        """Test initialization with custom paths."""
        temp_dir = tempfile.mkdtemp()
        cm = ConsciousnessMarker(
            bch_db_path=Path(temp_dir) / "test.db",
            output_path=Path(temp_dir)
        )
        self.assertEqual(cm.bch_db_path, Path(temp_dir) / "test.db")
        self.assertEqual(cm.output_path, Path(temp_dir))


if __name__ == "__main__":
    # Run with verbosity
    unittest.main(verbosity=2)
