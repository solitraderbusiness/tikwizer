class Task_id : public Task
  {
   string                PromptCaption;
   string                PromptText;
   int                PromptButtons;
public:
                     Task_id(string name):Task(name)
     {
      PromptCaption = (string)PromptCaption_val;
      PromptText = (string)PromptText_val;
      PromptButtons = (int)PromptButtons_val;
     }
   virtual void               run(int block_id, BlockParent &block)
     {
      Task::run(block_id, block);

      int code = MessageBox(PromptText, PromptCaption, PromptButtons);

      if(
         code == IDOK // OK
         || code == IDYES // Yes
         || code == IDRETRY // Retry
         || code == IDCONTINUE // Continue
      )
        {
         block.onResult(ROUTE_1_PASSED);
        }
      else
         if(
            code == IDABORT // Abort
            || code == IDNO // No
            || code == IDTRYAGAIN // Try Again
            || (code == IDCANCEL && (PromptButtons == MB_OKCANCEL || PromptButtons == MB_RETRYCANCEL)
               )
         )
           {
            block.onResult(ROUTE_2_PASSED);
           }

     }
   virtual void      reset(int level)
     {

     }
  };
