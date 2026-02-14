import { useState } from 'react';
import { EventTabBar } from '../editor/EventTabBar';
import { CodePreview } from '../editor/CodePreview';
import { AiChat } from '../ai/AiChat';
import { StrategySettings } from '../editor/StrategySettings';
import { generateMql } from '../../api/generate';
import { serializeStrategy } from '../../lib/serializer';

export function Header() {
  const [generatedCode, setGeneratedCode] = useState<string | null>(null);
  const [isGenerating, setIsGenerating] = useState(false);
  const [showAiChat, setShowAiChat] = useState(false);
  const [showSettings, setShowSettings] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleGenerate = async () => {
    setIsGenerating(true);
    setError(null);
    try {
      const strategy = serializeStrategy();
      const result = await generateMql(strategy);
      setGeneratedCode(result.code);
    } catch (e: any) {
      setError(e.message || 'Generation failed');
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <>
      <header
        className="flex items-center justify-between px-4 py-2 border-b"
        style={{ backgroundColor: 'var(--color-surface)', borderColor: 'var(--color-border)' }}
      >
        <div className="flex items-center gap-3">
          <h1 className="text-lg font-bold" style={{ color: 'var(--color-primary)' }}>
            Tikwizer
          </h1>
        </div>

        <EventTabBar />

        <div className="flex items-center gap-2">
          <button
            onClick={() => setShowSettings(true)}
            className="px-3 py-1.5 text-sm rounded border"
            style={{ borderColor: 'var(--color-border)', color: 'var(--color-text-muted)' }}
          >
            Settings
          </button>
          <button
            onClick={() => setShowAiChat(!showAiChat)}
            className="px-3 py-1.5 text-sm rounded border"
            style={{
              borderColor: showAiChat ? 'var(--color-primary)' : 'var(--color-border)',
              color: showAiChat ? 'var(--color-primary)' : 'var(--color-text-muted)',
            }}
          >
            AI Assistant
          </button>
          <button
            onClick={handleGenerate}
            disabled={isGenerating}
            className="px-4 py-1.5 text-sm font-medium text-white rounded disabled:opacity-50"
            style={{ backgroundColor: 'var(--color-primary)' }}
          >
            {isGenerating ? 'Generating...' : 'Generate MQL4'}
          </button>
        </div>
      </header>

      {error && (
        <div className="px-4 py-2 text-sm" style={{ backgroundColor: 'var(--color-accent-red)', color: 'white' }}>
          {error}
          <button onClick={() => setError(null)} className="ml-2 underline">Dismiss</button>
        </div>
      )}

      {generatedCode && (
        <CodePreview code={generatedCode} onClose={() => setGeneratedCode(null)} />
      )}

      {showAiChat && <AiChat onClose={() => setShowAiChat(false)} />}
      {showSettings && <StrategySettings onClose={() => setShowSettings(false)} />}
    </>
  );
}
