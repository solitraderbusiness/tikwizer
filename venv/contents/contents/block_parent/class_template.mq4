class BlockParent
  {
public:
   int               current_source_id;
   int               nexts_true[];//static, filled by generator
   int               nexts_false[];//static, filled by generator
   int               prevs_true[];//static, filled by generator
   int               prevs_false[];//static, filled by generator

public:
   virtual void      onResult(int result) = NULL;
  };
