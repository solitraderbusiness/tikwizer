import { Header } from './Header';
import { BlockPalette } from '../editor/BlockPalette';
import { Canvas } from '../editor/Canvas';
import { ConfigPanel } from '../editor/ConfigPanel';
import { VariablesPanel } from '../editor/VariablesPanel';
import { useEditorStore } from '../../stores/editorStore';
import { useStrategyStore } from '../../stores/strategyStore';

export function AppLayout() {
  const selectedNodeId = useEditorStore((s) => s.selectedNodeId);
  const selectedVarConst = useStrategyStore((s) => s.selectedVarConst);

  return (
    <div className="flex flex-col h-screen" style={{ backgroundColor: 'var(--color-bg)' }}>
      <Header />
      <div className="flex flex-1 overflow-hidden">
        <BlockPalette />
        <div className="flex-1 relative">
          <Canvas />
        </div>
        {selectedNodeId && !selectedVarConst && <ConfigPanel />}
        {selectedVarConst && <VariablesPanel />}
      </div>
    </div>
  );
}
