import { useCallback } from 'react';

interface CodePreviewProps {
  code: string;
  onClose: () => void;
}

export function CodePreview({ code, onClose }: CodePreviewProps) {
  const handleDownload = useCallback(() => {
    const blob = new Blob([code], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'expert_output.mq4';
    a.click();
    URL.revokeObjectURL(url);
  }, [code]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center" style={{ backgroundColor: 'rgba(0,0,0,0.7)' }}>
      <div
        className="w-[80vw] h-[80vh] rounded-lg flex flex-col shadow-2xl"
        style={{ backgroundColor: 'var(--color-surface)', border: '1px solid var(--color-border)' }}
      >
        {/* Header */}
        <div
          className="flex items-center justify-between px-4 py-3 border-b rounded-t-lg"
          style={{ borderColor: 'var(--color-border)', backgroundColor: 'var(--color-surface-light)' }}
        >
          <h2 className="text-sm font-semibold" style={{ color: 'var(--color-text)' }}>
            Generated MQL4 Code
          </h2>
          <div className="flex items-center gap-2">
            <span className="text-xs" style={{ color: 'var(--color-text-muted)' }}>
              {code.length.toLocaleString()} characters
            </span>
            <button
              onClick={handleDownload}
              className="px-3 py-1 text-sm rounded text-white"
              style={{ backgroundColor: 'var(--color-accent-green)' }}
            >
              Download .mq4
            </button>
            <button
              onClick={onClose}
              className="px-3 py-1 text-sm rounded border"
              style={{ borderColor: 'var(--color-border)', color: 'var(--color-text-muted)' }}
            >
              Close
            </button>
          </div>
        </div>

        {/* Code area */}
        <div className="flex-1 overflow-auto p-4">
          <pre
            className="text-xs leading-relaxed font-mono whitespace-pre"
            style={{ color: 'var(--color-text)' }}
          >
            {code}
          </pre>
        </div>
      </div>
    </div>
  );
}
