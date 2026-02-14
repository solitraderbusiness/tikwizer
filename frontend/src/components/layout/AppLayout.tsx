import { Header } from './Header';
import { BlockPalette } from '../editor/BlockPalette';
import { Canvas } from '../editor/Canvas';
import { ConfigPanel } from '../editor/ConfigPanel';
import { useEditorStore } from '../../stores/editorStore';

export function AppLayout() {
  const selectedNodeId = useEditorStore((s) => s.selectedNodeId);

  return (
    <div className="flex flex-col h-screen" style={{ backgroundColor: 'var(--color-bg)' }}>
      <Header />
      <div className="flex flex-1 overflow-hidden">
        <BlockPalette />
        <div className="flex-1 relative">
          <Canvas />
        </div>
        {selectedNodeId && <ConfigPanel />}
      </div>
    </div>
  );
}
