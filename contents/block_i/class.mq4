class Block0 : public Block
  {
public:
                     Block0()
     {
      id = 0;
      id_by_user = 25;
      name = "Block_0";
      enabled = true;
      event = EVENT_ON_TICK;

      int mnexts_true[] = {1,2};
      int mnexts_false[] = {};
      int mprevs_true[] = {};
      int mprevs_false[] = {};
      populateNextsTrue(mnexts_true);
      populateNextsFalse(mnexts_false);
      populatePrevsTrue(mprevs_true);
      populatePrevsFalse(mprevs_false);

      task = new Task0(name);
     }
  };
