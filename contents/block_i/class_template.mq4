class Block_id : public Block
  {
public:
                     Block_id()
     {
      id = id_val;
      id_by_user = id_by_user_val;
      name = name_val;
      enabled = enabled_val;
      event = event_val;

      int mnexts_true[] = nexts_true_val;
      int mnexts_false[] = nexts_false_val;
      int mprevs_true[] = prevs_true_val;
      int mprevs_false[] = prevs_false_val;
      populateNextsTrue(mnexts_true);
      populateNextsFalse(mnexts_false);
      populatePrevsTrue(mprevs_true);
      populatePrevsFalse(mprevs_false);

      task = new Task_id(name);
     }
  };
