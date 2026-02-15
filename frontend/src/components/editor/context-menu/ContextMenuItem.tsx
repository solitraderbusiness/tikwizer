interface ContextMenuItemProps {
  label: string;
  shortcut?: string;
  onClick: () => void;
  disabled?: boolean;
  danger?: boolean;
}

export function ContextMenuItem({ label, shortcut, onClick, disabled, danger }: ContextMenuItemProps) {
  return (
    <button
      className="flex w-full justify-between items-center px-3 py-1.5 text-sm disabled:opacity-40"
      style={{
        color: danger ? 'var(--color-accent-red)' : 'var(--color-text)',
        cursor: disabled ? 'default' : 'pointer',
      }}
      disabled={disabled}
      onClick={(e) => {
        e.stopPropagation();
        if (!disabled) onClick();
      }}
      onMouseEnter={(e) => {
        if (!disabled) {
          (e.currentTarget as HTMLElement).style.backgroundColor = 'var(--color-surface-light)';
        }
      }}
      onMouseLeave={(e) => {
        (e.currentTarget as HTMLElement).style.backgroundColor = 'transparent';
      }}
    >
      <span>{label}</span>
      {shortcut && (
        <span className="ml-4 text-xs" style={{ color: 'var(--color-text-muted)' }}>
          {shortcut}
        </span>
      )}
    </button>
  );
}
