import { ParamInput } from './ParamInput';
import { getFieldOptions } from './fieldOptions';

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
      {flatParams.map(([key, value]) => {
        const strValue = String(value);
        const options = getFieldOptions(key, strValue);

        return (
          <ParamInput
            key={key}
            label={formatLabel(key)}
            value={strValue}
            onChange={(v) => onChange({ [key]: v })}
            options={options ?? undefined}
          />
        );
      })}
    </div>
  );
}

/** Convert snake_case or camelCase field names to readable labels */
function formatLabel(key: string): string {
  return key
    // Insert space before uppercase letters (camelCase)
    .replace(/([a-z])([A-Z])/g, '$1 $2')
    // Replace underscores with spaces
    .replace(/_/g, ' ')
    // Capitalize first letter of each word
    .replace(/\b\w/g, (c) => c.toUpperCase());
}
