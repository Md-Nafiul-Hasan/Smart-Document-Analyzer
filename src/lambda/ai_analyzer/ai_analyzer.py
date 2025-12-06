"""DEPRECATED: use `src.lambdas.ai_analyzer.ai_analyzer` instead.

This module was duplicated under `src/lambda` during an earlier refactor.
Importing it will raise an ImportError to prevent accidental use.
"""

raise ImportError("DEPRECATED: import from 'src.lambdas.ai_analyzer.ai_analyzer' instead")
    
    def get_analysis_history(self) -> List[Dict[str, Any]]:
        """Get history of analyses performed."""
        return self.analysis_history
