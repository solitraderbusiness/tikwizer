interface GenericConfigProps {
  params: Record<string, any>;
  onChange: (params: Record<string, any>) => void;
}

export function GenericConfig({ params, onChange }: GenericConfigProps) {
  const flatParams = Object.entries(params).filter(([_, v]) => typeof v !== 'object');

  if (flatParams.length === 0) {
    return <p className="text-xs" style={{ color: 'var(--color-text-muted)' }}>No configurable parameters</p>;
  }

  return (
    <div className="space-y-3">
      {flatParams.map(([key, value]) => (
        <div key={key}>
          <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>
            {key.replace(/_/g, ' ')}
          </label>
          <input
            type="text"
            value={String(value)}
            onChange={(e) => onChange({ [key]: e.target.value })}
            className="w-full text-sm px-2 py-1.5 rounded border"
            style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
          />
        </div>
      ))}
    </div>
  );
}
