import { useStrategyStore } from '../../stores/strategyStore';

const INPUT_STYLE = {
  backgroundColor: 'var(--color-surface-light)',
  borderColor: 'var(--color-border)',
  color: 'var(--color-text)',
};

const TYPE_OPTIONS = ['double', 'int', 'string', 'bool'];

export function VariablesPanel() {
  const selectedVarConst = useStrategyStore((s) => s.selectedVarConst);
  const constants = useStrategyStore((s) => s.constants);
  const variables = useStrategyStore((s) => s.variables);
  const updateConstant = useStrategyStore((s) => s.updateConstant);
  const updateVariable = useStrategyStore((s) => s.updateVariable);
  const removeConstant = useStrategyStore((s) => s.removeConstant);
  const removeVariable = useStrategyStore((s) => s.removeVariable);
  const selectVarConst = useStrategyStore((s) => s.selectVarConst);

  if (!selectedVarConst) return null;

  const { kind, id } = selectedVarConst;
  const item = kind === 'constant'
    ? constants.find((c) => c.id === id)
    : variables.find((v) => v.id === id);

  if (!item) return null;

  const update = (data: Record<string, string>) => {
    if (kind === 'constant') updateConstant(id, data);
    else updateVariable(id, data);
  };

  const handleDelete = () => {
    if (kind === 'constant') removeConstant(id);
    else removeVariable(id);
    selectVarConst(null);
  };

  return (
    <div
      className="w-80 border-l overflow-y-auto flex-shrink-0"
      style={{ backgroundColor: 'var(--color-surface)', borderColor: 'var(--color-border)' }}
    >
      <div className="p-4">
        {/* Header */}
        <div className="flex items-center justify-between mb-4">
          <div>
            <h2 className="text-sm font-semibold" style={{ color: 'var(--color-text)' }}>
              {kind === 'constant' ? 'Constant' : 'Variable'}
            </h2>
            <span className="text-xs" style={{ color: 'var(--color-text-muted)' }}>
              {item.name || '(unnamed)'}
            </span>
          </div>
          <button
            onClick={handleDelete}
            className="text-xs px-2 py-1 rounded"
            style={{ color: '#ef4444', border: '1px solid #ef4444' }}
          >
            Delete
          </button>
        </div>

        {/* Form */}
        <div className="space-y-3">
          <div>
            <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Type</label>
            <select
              value={item.type}
              onChange={(e) => update({ type: e.target.value })}
              className="w-full text-sm px-2 py-1.5 rounded border"
              style={INPUT_STYLE}
            >
              {TYPE_OPTIONS.map((t) => <option key={t} value={t}>{t}</option>)}
            </select>
          </div>

          <div>
            <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Name</label>
            <input
              type="text"
              value={item.name}
              onChange={(e) => update({ name: e.target.value })}
              className="w-full text-sm px-2 py-1.5 rounded border"
              style={INPUT_STYLE}
              placeholder="e.g. max_trades"
            />
          </div>

          <div>
            <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>
              {kind === 'constant' ? 'Value' : 'Initial Value'}
            </label>
            <input
              type="text"
              value={item.value}
              onChange={(e) => update({ value: e.target.value })}
              className="w-full text-sm px-2 py-1.5 rounded border"
              style={INPUT_STYLE}
              placeholder="e.g. 10"
            />
          </div>

          <div>
            <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Description</label>
            <textarea
              value={item.description}
              onChange={(e) => update({ description: e.target.value })}
              rows={3}
              className="w-full text-sm px-2 py-1.5 rounded border resize-none"
              style={INPUT_STYLE}
              placeholder="Optional description..."
            />
          </div>
        </div>
      </div>
    </div>
  );
}
