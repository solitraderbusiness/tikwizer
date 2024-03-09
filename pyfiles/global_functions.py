TEMPLATE_ADD_BLOCKS = "Block_id *block_id = new Block_id();\n"
TEMPLATE_ADD_BLOCKS_FUNCTION = "blocks_tick[_id] = block_id;\n"


def get_fun__add_blocks_tick(n):
    result = "void addBlocksTick()\n{\nArrayResize(blocks_tick, blocks_size_val);\n"
    result = result.replace("blocks_size_val", str(n))
    for i in range(n):
        result += TEMPLATE_ADD_BLOCKS.replace("_id", str(i))
    result += "\n"
    for i in range(n):
        result += TEMPLATE_ADD_BLOCKS_FUNCTION.replace("_id", str(i))
    result += "  }\n"
    return result


def get_call__add_blocks_tick():
    result = "addBlocksTick();"
    return result


def get_fun__reset_blocks_tick():
    result = "void resetBlocksTick(int level)\n{\n    for(int i=0; i<ArraySize(blocks_tick); i++){\n        blocks_tick[i].reset(level);\n    }\n}"
    return result


def get_call__reset_blocks_tick():
    result = "resetBlocksTick(RESET_LEVEL_TICK);"
    return result


def get_fun__run_block_tick():
    result = "void runBlockTick(int source_id, int source_result, int dest_id)\n{\nblocks_tick[dest_id].run(source_id, source_result);\n}"
    return result


def get_call__run_block_tick(source_id, source_result, target_id):
    result = "runBlockTick(source_id_val, source_result_val, target_id_val);"
    result = result.replace("source_id_val", str(source_id)) \
        .replace("source_result_val", str(source_result)) \
        .replace("target_id_val", str(target_id))
    return result


def get_fun__remove_index_from_array():
    result = "template <typename T>\n void RemoveIndexFromArray(T& A[], int iPos) {\n int iLast;\n for(iLast = ArraySize(A) - 1; iPos < iLast; ++iPos)\n A[iPos] = A[iPos + 1];\n ArrayResize(A, iLast);\n }"
    return result


def get_fun__add_to_array():
    result = "template <typename T>\n void AddToArray(T& A[], T &value) {\n ArrayResize(A, ArraySize(A)+1);\n A[ArraySize(A)-1] = value;\n }"
    return result


def get_fun__join_arrays():
    result = "// Function to join two arrays into one\n void JoinArrays(const int& array1[], const int& array2[], int& arrayJoined[]) {\n int size1 = ArraySize(array1);\n int size2 = ArraySize(array2);\n int newSize = size1 + size2;\n ArrayCopy(arrayJoined, array1, 0, 0, size1);\n ArrayCopy(arrayJoined, array2, 0, size1, size2);\n }\n"
    return result


def get_fun__are_all_items_present():
    result = "// Check if all items in arrayB are in ArrayA\n bool areAllItemsPresent(int &arrayA[], int &arrayB[]) {\n for(int i = 0; i < ArraySize(arrayA); i++) {\n bool isPresent = false;\n for(int j = 0; j < ArraySize(arrayB); j++) {\n if(arrayA[i] == arrayB[j]) {\n isPresent = true;\n break;\n }\n }\n if(!isPresent) {\n return false;\n }\n } \nreturn true;\n }\n"
    return result


def get_fun__sync_symbol_overriding():
    result = "string syncSymbolOverriding(string symbol) {\n return overriding_symbol == \"\" ? symbol : overriding_symbol;\n}"
    return result


def get_fun__sync_timeframe_overriding():
    result = "int syncTimeframeOverriding(int timeframe) {\n return overriding_timeframe == -1 ? timeframe : overriding_timeframe;\n }"
    return result


def get_fun__time_from_string():
    result = "datetime TimeFromString(int mode_time, string stamp)\n  {\n   datetime t = 0;\n\n   if(mode_time == 0)\n      t = TimeCurrent();\n   else\n      if(mode_time == 1)\n         t = TimeLocal();\n      else\n         if(mode_time == 2)\n            t = TimeGMT();\n\n   int stamplen = StringLen(stamp);\n\n   if(stamplen < 9)\n     {\n      int thour    = TimeHour(t);\n      int tminute  = TimeMinute(t);\n      int tseconds = TimeSeconds(t);\n\n      int hour   = (int)StringSubstr(stamp, 0, 2);\n      int minute = (int)StringSubstr(stamp, 3, 2);\n      int second = 0;\n\n      if(stamplen > 5)\n        {\n         second = (int)StringSubstr(stamp, 6, 2);\n        }\n\n      datetime t1 = (datetime)(t - (thour-hour)*3600 - (tminute - minute)*60 - (tseconds-second));\n\n      return t1;\n     }\n\n   return StringToTime(stamp);\n  }\n\n"
    return result


def get_fun__time_from_components():
    result = "datetime TimeFromComponents(\n   int time_src = 0,\n   int    y = 0,\n   int    m = 0,\n   double d = 0,\n   double h = 0,\n   double i = 0,\n   int    s = 0\n)\n  {\n   MqlDateTime tm;\n   int offset = 0;\n\n   if(time_src == 0)\n     {\n      TimeCurrent(tm);\n     }\n   else\n      if(time_src == 1)\n        {\n         TimeLocal(tm);\n         offset = (int)(TimeLocal() - TimeCurrent());\n        }\n      else\n         if(time_src == 2)\n           {\n            TimeGMT(tm);\n            offset = (int)(TimeGMT() - TimeCurrent());\n           }\n\n   if(y > 0)\n     {\n      if(y < 100)\n        {\n         y = 2000 + y;\n        }\n      tm.year = y;\n     }\n   if(m > 0)\n     {\n      tm.mon = m;\n     }\n   if(d > 0)\n     {\n      tm.day = (int)MathFloor(d);\n     }\n\n   tm.hour = (int)(MathFloor(h) + (24 * (d - MathFloor(d))));\n   tm.min  = (int)(MathFloor(i) + (60 * (h - MathFloor(h))));\n   tm.sec  = (int)((double)s + (60 * (i - MathFloor(i))));\n\n   datetime time = StructToTime(tm) - offset;\n\n   return time;\n  }\n"
    return result


def get_fun__seconds_from_components():
    result = "int SecondsFromComponents(double days, double hours, double minutes, int seconds)\n  {\n   int retval =\n      86400 * (int)MathFloor(days)\n      + 3600 * (int)(MathFloor(hours) + (24 * (days - MathFloor(days))))\n      + 60 * (int)(MathFloor(minutes) + (60 * (hours - MathFloor(hours))))\n      + (int)((double)seconds + (60 * (minutes - MathFloor(minutes))));\n\n   return retval;\n  }\n"
    return result


def get_fun__get_group_number():
    result = "//Considering each magic number is a 7 digit number like 2088100,\n//I choose to take first two digits as group number.\nint getGroupNumber (int magic){\n   return (int)(magic/100000);\n}"
    return result


def get_fun__same_order_type():
    result = "//This just checks if order is buy or sell\nbool sameOrderType (int type[], int orderType){\n   for (int i=0; i<ArraySize(type); i++)\n      if (orderType==type[i])\n         return true;\n   return false;\n}"
    return result


def get_fun__is_automated():
    result = "//72 is the number in magic 3rd and 4th\n//digits that show it is opened by the expert\nbool isAutomated (int magic){\n   return MathMod((int)(magic/1000), 100) == 72;\n}\n"
    return result


def get_fun__reverse_list():
    result = "void ReverseList(int &arr[])\n  {\n   int size = ArraySize(arr);\n   ArraySetAsSeries(arr, true);\n\n   for(int i = 0; i < size / 2; i++)\n     {\n      int temp = arr[i];\n      arr[i] = arr[size - 1 - i];\n      arr[size - 1 - i] = temp;\n     }\n  }\n"
    return result


def get_fun__sleepex():
    result = "#import \"kernel32.dll\"\nbool SleepEx(int ms, bool bAlertable);\n#import\n\n"
    return result


def get_fun__delete_order():
    result = "bool DeleteOrder(ulong ticket, color arrowcolor=clrNONE)\n  {\n   bool success=false;\n   if(!OrderSelect((int)ticket,SELECT_BY_TICKET,MODE_TRADES))\n     {\n      return(false);\n     }\n\n   while(true)\n     {\n      //-- wait if needed -----------------------------------------------\n      WaitTradeContextIfBusy();\n      //-- delete -------------------------------------------------------\n      success=OrderDelete((int)ticket,arrowcolor);\n      //-- error check --------------------------------------------------\n      int erraction=CheckForTradingError(GetLastError(), \"Deleting order #\"+(string)ticket+\" error\");\n      switch(erraction)\n        {\n         case 0:\n            break;    // no error\n         case 1:\n            continue; // overcomable error\n         case 2:\n            break;    // fatal error\n        }\n      break;\n     }\n   return(false);\n  }\n\n"
    return result


def get_fun__wait_trade_context_if_busy():
    result = "void WaitTradeContextIfBusy()\n  {\n   if(IsTradeContextBusy())\n     {\n      while(true)\n        {\n         Sleep(1);\n         if(!IsTradeContextBusy())\n           {\n            RefreshRates();\n            break;\n           }\n        }\n     }\n   return;\n  }\n"
    return result


def get_fun__check_for_trading_error():
    result = "int CheckForTradingError(int error_code=-1, string msg_prefix=\"\")\n  {\n// return 0 -> no error\n// return 1 -> overcomable error\n// return 2 -> fatal error\n\n   if(error_code<0)\n     {\n      error_code=GetLastError();\n     }\n\n   int retval=0;\n   static int tryouts=0;\n\n//-- error check -----------------------------------------------------\n   switch(error_code)\n     {\n      //-- no error\n      case 0:\n         retval=0;\n         break;\n      //-- overcomable errors\n      case 1: // No error returned\n         RefreshRates();\n         retval=1;\n         break;\n      case 4: //ERR_SERVER_BUSY\n         if(msg_prefix!=\"\")\n           {\n            Print(StringConcatenate(msg_prefix,\": \",ErrorMessage(error_code),\". Retrying..\"));\n           }\n         Sleep(1000);\n         RefreshRates();\n         retval=1;\n         break;\n      case 6: //ERR_NO_CONNECTION\n         if(msg_prefix!=\"\")\n           {\n            Print(StringConcatenate(msg_prefix,\": \",ErrorMessage(error_code),\". Retrying..\"));\n           }\n         while(!IsConnected())\n           {\n            Sleep(100);\n           }\n         while(IsTradeContextBusy())\n           {\n            Sleep(50);\n           }\n         RefreshRates();\n         retval=1;\n         break;\n      case 128: //ERR_TRADE_TIMEOUT\n         if(msg_prefix!=\"\")\n           {\n            Print(StringConcatenate(msg_prefix,\": \",ErrorMessage(error_code),\". Retrying..\"));\n           }\n         RefreshRates();\n         retval=1;\n         break;\n      case 129: //ERR_INVALID_PRICE\n         if(msg_prefix!=\"\")\n           {\n            Print(StringConcatenate(msg_prefix,\": \",ErrorMessage(error_code),\". Retrying..\"));\n           }\n         if(!IsTesting())\n           {\n            while(RefreshRates()==false)\n              {\n               Sleep(1);\n              }\n           }\n         retval=1;\n         break;\n      case 130: //ERR_INVALID_STOPS\n         if(msg_prefix!=\"\")\n           {\n            Print(StringConcatenate(msg_prefix,\": \",ErrorMessage(error_code),\". Waiting for a new tick to retry..\"));\n           }\n         if(!IsTesting())\n           {\n            while(RefreshRates()==false)\n              {\n               Sleep(1);\n              }\n           }\n         retval=1;\n         break;\n      case 135: //ERR_PRICE_CHANGED\n         if(msg_prefix!=\"\")\n           {\n            Print(StringConcatenate(msg_prefix,\": \",ErrorMessage(error_code),\". Waiting for a new tick to retry..\"));\n           }\n         if(!IsTesting())\n           {\n            while(RefreshRates()==false)\n              {\n               Sleep(1);\n              }\n           }\n         retval=1;\n         break;\n      case 136: //ERR_OFF_QUOTES\n         if(msg_prefix!=\"\")\n           {\n            Print(StringConcatenate(msg_prefix,\": \",ErrorMessage(error_code),\". Waiting for a new tick to retry..\"));\n           }\n         if(!IsTesting())\n           {\n            while(RefreshRates()==false)\n              {\n               Sleep(1);\n              }\n           }\n         retval=1;\n         break;\n      case 137: //ERR_BROKER_BUSY\n         if(msg_prefix!=\"\")\n           {\n            Print(StringConcatenate(msg_prefix,\": \",ErrorMessage(error_code),\". Retrying..\"));\n           }\n         Sleep(1000);\n         retval=1;\n         break;\n      case 138: //ERR_REQUOTE\n         if(msg_prefix!=\"\")\n           {\n            Print(StringConcatenate(msg_prefix,\": \",ErrorMessage(error_code),\". Waiting for a new tick to retry..\"));\n           }\n         if(!IsTesting())\n           {\n            while(RefreshRates()==false)\n              {\n               Sleep(1);\n              }\n           }\n         retval=1;\n         break;\n      case 142: //This code should be processed in the same way as error 128.\n         if(msg_prefix!=\"\")\n           {\n            Print(StringConcatenate(msg_prefix,\": \",ErrorMessage(error_code),\". Retrying..\"));\n           }\n         RefreshRates();\n         retval=1;\n         break;\n      case 143: //This code should be processed in the same way as error 128.\n         if(msg_prefix!=\"\")\n           {\n            Print(StringConcatenate(msg_prefix,\": \",ErrorMessage(error_code),\". Retrying..\"));\n           }\n         RefreshRates();\n         retval=1;\n         break;\n      /*case 145: //ERR_TRADE_MODIFY_DENIED\n         if (msg_prefix!=\"\") {Print(StringConcatenate(msg_prefix,\": \",ErrorMessage(error_code),\". Waiting for a new tick to retry..\"));}\n         while(RefreshRates()==false) {Sleep(1);}\n         return(1);\n      */\n      case 146: //ERR_TRADE_CONTEXT_BUSY\n         if(msg_prefix!=\"\")\n           {\n            Print(StringConcatenate(msg_prefix,\": \",ErrorMessage(error_code),\". Retrying..\"));\n           }\n         while(IsTradeContextBusy())\n           {\n            Sleep(50);\n           }\n         RefreshRates();\n         retval=1;\n         break;\n      //-- critical errors\n      default:\n         if(msg_prefix!=\"\")\n           {\n            Print(StringConcatenate(msg_prefix,\": \",ErrorMessage(error_code)));\n           }\n         retval=2;\n         break;\n     }\n\n   if(retval==0)\n     {\n      tryouts=0;\n     }\n   else\n      if(retval==1)\n        {\n         tryouts++;\n         if(tryouts>=10)\n           {\n            tryouts=0;\n            retval=2;\n           }\n         else\n           {\n            Print(\"retry #\"+(string)tryouts+\" of 10\");\n           }\n        }\n\n   return(retval);\n  }\n"
    return result


def get_fun__error_message():
    result = "string ErrorMessage(int error_code=-1)\n  {\n   string e = \"\";\n\n   if(error_code < 0)\n     {\n      error_code = GetLastError();\n     }\n\n   switch(error_code)\n     {\n      //-- codes returned from trade server\n      case 0:\n         return(\"\");\n      case 1:\n         e = \"No error returned\";\n         break;\n      case 2:\n         e = \"Common error\";\n         break;\n      case 3:\n         e = \"Invalid trade parameters\";\n         break;\n      case 4:\n         e = \"Trade server is busy\";\n         break;\n      case 5:\n         e = \"Old version of the client terminal\";\n         break;\n      case 6:\n         e = \"No connection with trade server\";\n         break;\n      case 7:\n         e = \"Not enough rights\";\n         break;\n      case 8:\n         e = \"Too frequent requests\";\n         break;\n      case 9:\n         e = \"Malfunctional trade operation (never returned error)\";\n         break;\n      case 64:\n         e = \"Account disabled\";\n         break;\n      case 65:\n         e = \"Invalid account\";\n         break;\n      case 128:\n         e = \"Trade timeout\";\n         break;\n      case 129:\n         e = \"Invalid price\";\n         break;\n      case 130:\n         e = \"Invalid Sl or TP\";\n         break;\n      case 131:\n         e = \"Invalid trade volume\";\n         break;\n      case 132:\n         e = \"Market is closed\";\n         break;\n      case 133:\n         e = \"Trade is disabled\";\n         break;\n      case 134:\n         e = \"Not enough money\";\n         break;\n      case 135:\n         e = \"Price changed\";\n         break;\n      case 136:\n         e = \"Off quotes\";\n         break;\n      case 137:\n         e = \"Broker is busy (never returned error)\";\n         break;\n      case 138:\n         e = \"Requote\";\n         break;\n      case 139:\n         e = \"Order is locked\";\n         break;\n      case 140:\n         e = \"Only long trades allowed\";\n         break;\n      case 141:\n         e = \"Too many requests\";\n         break;\n      case 145:\n         e = \"Modification denied because order too close to market\";\n         break;\n      case 146:\n         e = \"Trade context is busy\";\n         break;\n      case 147:\n         e = \"Expirations are denied by broker\";\n         break;\n      case 148:\n         e = \"Amount of open and pending orders has reached the limit\";\n         break;\n      case 149:\n         e = \"Hedging is prohibited\";\n         break;\n      case 150:\n         e = \"Prohibited by FIFO rules\";\n         break;\n\n      //-- mql4 errors\n      case 4000:\n         e = \"No error\";\n         break;\n      case 4001:\n         e = \"Wrong function pointer\";\n         break;\n      case 4002:\n         e = \"Array index is out of range\";\n         break;\n      case 4003:\n         e = \"No memory for function call stack\";\n         break;\n      case 4004:\n         e = \"Recursive stack overflow\";\n         break;\n      case 4005:\n         e = \"Not enough stack for parameter\";\n         break;\n      case 4006:\n         e = \"No memory for parameter string\";\n         break;\n      case 4007:\n         e = \"No memory for temp string\";\n         break;\n      case 4008:\n         e = \"Not initialized string\";\n         break;\n      case 4009:\n         e = \"Not initialized string in array\";\n         break;\n      case 4010:\n         e = \"No memory for array string\";\n         break;\n      case 4011:\n         e = \"Too long string\";\n         break;\n      case 4012:\n         e = \"Remainder from zero divide\";\n         break;\n      case 4013:\n         e = \"Zero divide\";\n         break;\n      case 4014:\n         e = \"Unknown command\";\n         break;\n      case 4015:\n         e = \"Wrong jump\";\n         break;\n      case 4016:\n         e = \"Not initialized array\";\n         break;\n      case 4017:\n         e = \"dll calls are not allowed\";\n         break;\n      case 4018:\n         e = \"Cannot load library\";\n         break;\n      case 4019:\n         e = \"Cannot call function\";\n         break;\n      case 4020:\n         e = \"Expert function calls are not allowed\";\n         break;\n      case 4021:\n         e = \"Not enough memory for temp string returned from function\";\n         break;\n      case 4022:\n         e = \"System is busy\";\n         break;\n      case 4050:\n         e = \"Invalid function parameters count\";\n         break;\n      case 4051:\n         e = \"Invalid function parameter value\";\n         break;\n      case 4052:\n         e = \"String function internal error\";\n         break;\n      case 4053:\n         e = \"Some array error\";\n         break;\n      case 4054:\n         e = \"Incorrect series array using\";\n         break;\n      case 4055:\n         e = \"Custom indicator error\";\n         break;\n      case 4056:\n         e = \"Arrays are incompatible\";\n         break;\n      case 4057:\n         e = \"Global variables processing error\";\n         break;\n      case 4058:\n         e = \"Global variable not found\";\n         break;\n      case 4059:\n         e = \"Function is not allowed in testing mode\";\n         break;\n      case 4060:\n         e = \"Function is not confirmed\";\n         break;\n      case 4061:\n         e = \"Send mail error\";\n         break;\n      case 4062:\n         e = \"String parameter expected\";\n         break;\n      case 4063:\n         e = \"Integer parameter expected\";\n         break;\n      case 4064:\n         e = \"Double parameter expected\";\n         break;\n      case 4065:\n         e = \"Array as parameter expected\";\n         break;\n      case 4066:\n         e = \"Requested history data in update state\";\n         break;\n      case 4099:\n         e = \"End of file\";\n         break;\n      case 4100:\n         e = \"Some file error\";\n         break;\n      case 4101:\n         e = \"Wrong file name\";\n         break;\n      case 4102:\n         e = \"Too many opened files\";\n         break;\n      case 4103:\n         e = \"Cannot open file\";\n         break;\n      case 4104:\n         e = \"Incompatible access to a file\";\n         break;\n      case 4105:\n         e = \"No order selected\";\n         break;\n      case 4106:\n         e = \"Unknown symbol\";\n         break;\n      case 4107:\n         e = \"Invalid price parameter for trade function\";\n         break;\n      case 4108:\n         e = \"Invalid ticket\";\n         break;\n      case 4109:\n         e = \"Trade is not allowed in the expert properties\";\n         break;\n      case 4110:\n         e = \"Longs are not allowed in the expert properties\";\n         break;\n      case 4111:\n         e = \"Shorts are not allowed in the expert properties\";\n         break;\n\n      //-- objects errors\n      case 4200:\n         e = \"Object is already exist\";\n         break;\n      case 4201:\n         e = \"Unknown object property\";\n         break;\n      case 4202:\n         e = \"Object is not exist\";\n         break;\n      case 4203:\n         e = \"Unknown object type\";\n         break;\n      case 4204:\n         e = \"No object name\";\n         break;\n      case 4205:\n         e = \"Object coordinates error\";\n         break;\n      case 4206:\n         e = \"No specified subwindow\";\n         break;\n      case 4207:\n         e = \"Graphical object error\";\n         break;\n      case 4210:\n         e = \"Unknown chart property\";\n         break;\n      case 4211:\n         e = \"Chart not found\";\n         break;\n      case 4212:\n         e = \"Chart subwindow not found\";\n         break;\n      case 4213:\n         e = \"Chart indicator not found\";\n         break;\n      case 4220:\n         e = \"Symbol select error\";\n         break;\n      case 4250:\n         e = \"Notification error\";\n         break;\n      case 4251:\n         e = \"Notification parameter error\";\n         break;\n      case 4252:\n         e = \"Notifications disabled\";\n         break;\n      case 4253:\n         e = \"Notification send too frequent\";\n         break;\n\n      //-- ftp errors\n      case 4260:\n         e = \"FTP server is not specified\";\n         break;\n      case 4261:\n         e = \"FTP login is not specified\";\n         break;\n      case 4262:\n         e = \"FTP connection failed\";\n         break;\n      case 4263:\n         e = \"FTP connection closed\";\n         break;\n      case 4264:\n         e = \"FTP path not found on server\";\n         break;\n      case 4265:\n         e = \"File not found in the MQL4\\\\Files directory to send on FTP server\";\n         break;\n      case 4266:\n         e = \"Common error during FTP data transmission\";\n         break;\n\n      //-- filesystem errors\n      case 5001:\n         e = \"Too many opened files\";\n         break;\n      case 5002:\n         e = \"Wrong file name\";\n         break;\n      case 5003:\n         e = \"Too long file name\";\n         break;\n      case 5004:\n         e = \"Cannot open file\";\n         break;\n      case 5005:\n         e = \"Text file buffer allocation error\";\n         break;\n      case 5006:\n         e = \"Cannot delete file\";\n         break;\n      case 5007:\n         e = \"Invalid file handle (file closed or was not opened)\";\n         break;\n      case 5008:\n         e = \"Wrong file handle (handle index is out of handle table)\";\n         break;\n      case 5009:\n         e = \"File must be opened with FILE_WRITE flag\";\n         break;\n      case 5010:\n         e = \"File must be opened with FILE_READ flag\";\n         break;\n      case 5011:\n         e = \"File must be opened with FILE_BIN flag\";\n         break;\n      case 5012:\n         e = \"File must be opened with FILE_TXT flag\";\n         break;\n      case 5013:\n         e = \"File must be opened with FILE_TXT or FILE_CSV flag\";\n         break;\n      case 5014:\n         e = \"File must be opened with FILE_CSV flag\";\n         break;\n      case 5015:\n         e = \"File read error\";\n         break;\n      case 5016:\n         e = \"File write error\";\n         break;\n      case 5017:\n         e = \"String size must be specified for binary file\";\n         break;\n      case 5018:\n         e = \"Incompatible file (for string arrays-TXT, for others-BIN)\";\n         break;\n      case 5019:\n         e = \"File is directory, not file\";\n         break;\n      case 5020:\n         e = \"File does not exist\";\n         break;\n      case 5021:\n         e = \"File cannot be rewritten\";\n         break;\n      case 5022:\n         e = \"Wrong directory name\";\n         break;\n      case 5023:\n         e = \"Directory does not exist\";\n         break;\n      case 5024:\n         e = \"Specified file is not directory\";\n         break;\n      case 5025:\n         e = \"Cannot delete directory\";\n         break;\n      case 5026:\n         e = \"Cannot clean directory\";\n         break;\n\n      //-- other errors\n      case 5027:\n         e = \"Array resize error\";\n         break;\n      case 5028:\n         e = \"String resize error\";\n         break;\n      case 5029:\n         e = \"Structure contains strings or dynamic arrays\";\n         break;\n\n      //-- http request\n      case 5200:\n         e = \"Invalid URL\";\n         break;\n      case 5201:\n         e = \"Failed to connect to specified URL\";\n         break;\n      case 5202:\n         e = \"Timeout exceeded\";\n         break;\n      case 5203:\n         e = \"HTTP request failed\";\n         break;\n\n      default:\n         e = \"Unknown error\";\n     }\n\n   e = StringConcatenate(e, \" (\", error_code, \")\");\n\n   return e;\n  }"
    return result


def get_fun__bet_martingale():
    result = "double BetMartingale(\n   string symbol,\n   int look_up_on,\n   int group,\n   int &type[],\n   double initialLots,\n   double multiplyOnLoss,\n   double multiplyOnProfit,\n   double addOnLoss,\n   double addOnProfit,\n   int resetOnLoss,\n   int resetOnProfit\n)\n  {\n   double info[];\n   GetBetTradesInfo(info, symbol, look_up_on, group, type, true);\n\n   double lots         = info[0];\n   double profitOrLoss = info[1]; // 0 - unknown, 1 - profit, -1 - loss\n   double consecutive  = info[2];\n\n//-- Martingale Logic\n   if(lots == 0)\n     {\n      lots = initialLots;\n     }\n   else\n     {\n      if(profitOrLoss == 1)\n        {\n         if(resetOnProfit > 0 && consecutive >= resetOnProfit)\n           {\n            lots = initialLots;\n           }\n         else\n           {\n            if(multiplyOnProfit <= 0)\n              {\n               multiplyOnProfit = 1;\n              }\n\n            lots = (lots * multiplyOnProfit) + addOnProfit;\n           }\n        }\n      else\n        {\n         if(resetOnLoss > 0 && consecutive >= resetOnLoss)\n           {\n            lots = initialLots;\n           }\n         else\n           {\n            if(multiplyOnLoss <= 0)\n              {\n               multiplyOnLoss = 1;\n              }\n\n            lots = (lots * multiplyOnLoss) + addOnLoss;\n           }\n        }\n     }\n\n   return lots;\n  }"
    return result


def get_fun__get_bet_trades_info():
    result = "void GetBetTradesInfo(\n   double &output[],\n   string symbol,\n   int look_up_on, // 0: try running trades first and then history trades, 1: try running only, 2: try history only\n   int group,\n   int &type[],\n   bool findConsecutive = false\n)\n  {\n   if(ArraySize(output) < 4)\n     {\n      ArrayResize(output, 4);\n      ArrayInitialize(output, 0.0);\n     }\n\n   double lots         = output[0]; // will be the lot size of the first loaded trade\n   double profitOrLoss = output[1]; // 0 is initial value, 1 is profit, -1 is loss\n   double consecutive  = output[2]; // the number of consecutive profitable or losable trades\n   double profit       = output[3]; // will be the profit of the first loaded trade\n   bool historyTrades  = look_up_on == LOOK_UP_RUNNING_ONLY ? false : true;\n\n   int total = (historyTrades) ? OrdersHistoryTotal() : OrdersTotal();\n\n   for(int pos = total - 1; pos >= 0; pos--)\n     {\n      bool con1 = !historyTrades && TradeSelectByIndex(pos, ORDER_GROUP_MODE_NUMBER, group, symbol, type);\n      bool con2 = historyTrades && HistoryTradeSelectByIndex(pos, ORDER_GROUP_MODE_NUMBER, group, symbol, type);\n      if(con1 || con2)\n        {\n         bool skipCon1 = ((look_up_on == 0 || look_up_on == 1) && TimeCurrent() - OrderOpenTime() < 3); // skip for brand new trades\n         bool skipCon2 = !historyTrades && OrderExpiration() > 0 && OrderExpiration() <= OrderCloseTime(); // exclude expired pending orders\n         if(skipCon1 || skipCon2)\n            continue;\n         if(lots == 0.0)\n           {\n            lots = OrderLots();\n           }\n\n         profit = OrderClosePrice() - OrderOpenPrice();\n         profit = NormalizeDouble(profit, SymbolDigits(OrderSymbol()));\n\n         if(profit == 0.0)\n           {\n            // Consider a trade with zero profit as non existent\n            continue;\n           }\n\n         if(IsOrderTypeSell())\n           {\n            profit = -1 * profit;\n           }\n\n         if(profitOrLoss == 0)\n           {\n            // We enter here only for the first trade\n            profitOrLoss = (profit < 0.0) ? -1 : 1;\n\n            consecutive++;\n            if(findConsecutive == false)\n               break;\n           }\n         else\n           {\n            // For the trades after the first one, if its profit is the opposite of profitOrLoss, we need to break\n            if(\n               (profitOrLoss > 0.0 && profit < 0.0)\n               || (profitOrLoss < 0.0 && profit > 0.0)\n            )\n              {\n               break;\n              }\n\n            consecutive++;\n           }\n        }\n     }\n\n   output[0] = lots;\n   output[1] = profitOrLoss;\n   output[2] = consecutive;\n   output[3] = profit;\n\n   if(look_up_on == 0 && (findConsecutive || profitOrLoss == 0))\n     {\n      // running trades tried, continue with the history trades\n      look_up_on = 2;\n      GetBetTradesInfo(output, symbol, look_up_on, group, type, findConsecutive);\n     }\n  }\n"
    return result


def get_fun__trade_select_by_index():
    result = "bool TradeSelectByIndex(\n   int index,\n   string group_mode,\n   string group,\n   string msymbol,\n   int type[]\n)\n  {\n   if(OrderSelect(index, SELECT_BY_POS, MODE_TRADES))\n     {\n      bool x = filterGeneral(msymbol, type, group_mode, group);\n      return x;\n     }\n\n   return false;\n\n\n\n  }"
    return result


def get_fun__history_trade_select_by_index():
    result = "bool HistoryTradeSelectByIndex(\n   int index,\n   string group_mode,\n   string group,\n   string msymbol,\n   int type[]\n)\n  {\n   if(OrderSelect((int)index, SELECT_BY_POS, MODE_HISTORY) && OrderType() < 2)\n     {\n      bool x = filterGeneral(msymbol, type, group_mode, group);\n      return x;\n     }\n\n   return false;\n  }\n"
    return result


def get_fun__filter_general():
    result = "bool              filterGeneral(string symbol, int type[], int group_mode, int group_number)\n  {\n   bool con1 = (symbol==NULL && OrderSymbol()==Symbol()) || symbol==OrderSymbol();\n   bool con2 = sameOrderType(type, OrderType());\n   bool con3 = group_mode!=ORDER_GROUP_MODE_NUMBER || group_number==getGroupNumber(OrderMagicNumber());\n   bool con4 = group_mode!=ORDER_GROUP_MODE_AUTOMATED || isAutomated(OrderMagicNumber());\n   return con1 && con2 && con3 && con4;\n  }\n"
    return result


def get_fun__symbol_digits():
    result = "int SymbolDigits(string symbol)\n  {\n   if(symbol == \"\")\n      symbol = Symbol();\n\n   return (int)SymbolInfoInteger(symbol, SYMBOL_DIGITS);\n  }"
    return result


def get_fun__is_order_type_sell():
    result = "bool IsOrderTypeSell()\n  {\n   int type = OrderType();\n\n   return (type == OP_SELL || type == OP_SELLSTOP || type == OP_SELLLIMIT);\n  }"
    return result


def get_fun__dynamic_lots():
    result = "double DynamicLots(string symbol, int mode, double value=0, double sl=0, string align=\"align\", double RJFR_initial_lots=0)\n  {\n   double size=0;\n   double LotStep=MarketInfo(symbol,MODE_LOTSTEP);\n   double LotSize=MarketInfo(symbol,MODE_LOTSIZE);\n   double MinLots=MarketInfo(symbol,MODE_MINLOT);\n   double MaxLots=MarketInfo(symbol,MODE_MAXLOT);\n   double TickValue=MarketInfo(symbol,MODE_TICKVALUE);\n   double point=MarketInfo(symbol,MODE_POINT);\n   double ticksize=MarketInfo(symbol,MODE_TICKSIZE);\n   double margin_required=MarketInfo(symbol,MODE_MARGINREQUIRED);\n\n   if(mode==MONEY_MANAGEMENT_FIXED_VOLUME)\n     {\n      size=value;\n\n     }\n   else\n      if(mode==MONEY_MANAGEMENT_PERCENT_OF_EQUITY)\n        {\n         size=(value/100)*AccountEquity()/margin_required;\n        }\n      else\n         if(mode==MONEY_MANAGEMENT_PERCENT_OF_BALANCE)\n           {\n            size=(value/100)*AccountBalance()/margin_required;\n           }\n         else\n            if(mode==MONEY_MANAGEMENT_PERCENT_OF_FREE_MARGIN)\n              {\n               size=(value/100)*AccountFreeMargin()/margin_required;\n              }\n            else\n               if(mode==MONEY_MANAGEMENT_FREEZE_PERCENT_OF_EQUITY)\n                 {\n                  size=(value/100)*AccountEquity()/(LotSize*TickValue);\n                 }\n               else\n                  if(mode==MONEY_MANAGEMENT_FREEZE_PERCENT_OF_BALANCE)\n                    {\n                     size=(value/100)*AccountBalance()/(LotSize*TickValue);\n                    }\n                  else\n                     if(mode==MONEY_MANAGEMENT_FREEZE_PERCENT_OF_FREE_MARGIN)\n                       {\n                        size=(value/100)*AccountFreeMargin()/(LotSize*TickValue);\n                       }\n                     else\n                        if(mode==MONEY_MANAGEMENT_RISK_PERCENT_OF_EQUITY)\n                          {\n                           size=((value/100)*AccountEquity())/(sl*((TickValue/ticksize)*point)*PipValue(symbol));\n                          }\n                        else\n                           if(mode==MONEY_MANAGEMENT_RISK_PERCENT_OF_BALANCE)\n                             {\n                              size=((value/100)*AccountBalance())/(sl*((TickValue/ticksize)*point)*PipValue(symbol));\n                             }\n                           else\n                              if(mode==MONEY_MANAGEMENT_RISK_PERCENT_OF_FREE_MARGIN)\n                                {\n                                 size=((value/100)*AccountFreeMargin())/(sl*((TickValue/ticksize)*point)*PipValue(symbol));\n                                }\n                              else\n                                 if(mode==\"fixedRisk\")\n                                   {\n                                    size=(value)/(sl*((TickValue/ticksize)*point)*PipValue(symbol));\n                                   }\n                                 else\n                                    if(mode==\"fixedRatio\" || mode==\"RJFR\")\n                                      {\n\n                                       /////\n                                       // Ryan Jones Fixed Ratio MM static data\n                                       static double RJFR_start_lots=0;\n                                       static double RJFR_delta=0;\n                                       static double RJFR_units=1;\n                                       static double RJFR_target_lower=0;\n                                       static double RJFR_target_upper=0;\n                                       /////\n\n                                       if(RJFR_start_lots<=0)\n                                         {\n                                          RJFR_start_lots=value;\n                                         }\n                                       if(RJFR_start_lots<MinLots)\n                                         {\n                                          RJFR_start_lots=MinLots;\n                                         }\n                                       if(RJFR_delta<=0)\n                                         {\n                                          RJFR_delta=sl;\n                                         }\n                                       if(RJFR_target_upper<=0)\n                                         {\n                                          RJFR_target_upper=AccountEquity()+(RJFR_units*RJFR_delta);\n                                          Print(\"Fixed Ratio MM: Units=>\",RJFR_units,\"; Delta=\",RJFR_delta,\"; Upper Target Equity=>\",RJFR_target_upper);\n                                         }\n                                       if(AccountEquity()>=RJFR_target_upper)\n                                         {\n                                          while(true)\n                                            {\n                                             Print(\"Fixed Ratio MM going up to \",(RJFR_start_lots*(RJFR_units+1)),\" lots: Equity is above Upper Target Equity (\",AccountEquity(),\">=\",RJFR_target_upper,\")\");\n                                             RJFR_units++;\n                                             RJFR_target_lower=RJFR_target_upper;\n                                             RJFR_target_upper=RJFR_target_upper+(RJFR_units*RJFR_delta);\n                                             Print(\"Fixed Ratio MM: Units=>\",RJFR_units,\"; Delta=\",RJFR_delta,\"; Lower Target Equity=>\",RJFR_target_lower,\"; Upper Target Equity=>\",RJFR_target_upper);\n                                             if(AccountEquity()<RJFR_target_upper)\n                                               {\n                                                break;\n                                               }\n                                            }\n                                         }\n                                       else\n                                          if(AccountEquity()<=RJFR_target_lower)\n                                            {\n                                             while(true)\n                                               {\n                                                if(AccountEquity()>RJFR_target_lower)\n                                                  {\n                                                   break;\n                                                  }\n                                                if(RJFR_units>1)\n                                                  {\n                                                   Print(\"Fixed Ratio MM going down to \",(RJFR_start_lots*(RJFR_units-1)),\" lots: Equity is below Lower Target Equity | \", AccountEquity(),\" <= \",RJFR_target_lower,\")\");\n                                                   RJFR_target_upper=RJFR_target_lower;\n                                                   RJFR_target_lower=RJFR_target_lower-((RJFR_units-1)*RJFR_delta);\n                                                   RJFR_units--;\n                                                   Print(\"Fixed Ratio MM: Units=>\",RJFR_units,\"; Delta=\",RJFR_delta,\"; Lower Target Equity=>\",RJFR_target_lower,\"; Upper Target Equity=>\",RJFR_target_upper);\n                                                  }\n                                                else\n                                                  {\n                                                   break;\n                                                  }\n                                               }\n                                            }\n                                       size=RJFR_start_lots*RJFR_units;\n                                      }\n   if(size==EMPTY_VALUE)\n     {\n      size=0;\n     }\n\n   size=MathRound(size/LotStep)*LotStep;\n   return (size);\n  }\n"
    return result


def get_fun__pip_value():
    result = "double PipValue(string symbol)\n  {\n   if(symbol == \"\")\n      symbol = Symbol();\n\n   return CustomPoint(symbol) / SymbolInfoDouble(symbol, SYMBOL_POINT);\n  }"
    return result


def get_fun__custom_point():
    result = "double CustomPoint(string symbol)\n  {\n   static string symbols[];\n   static double points[];\n   static string last_symbol = \"-\";\n   static double last_point  = 0;\n   static int last_i         = 0;\n   static int size           = 0;\n\n//-- variant A) use the cache for the last used symbol\n   if(symbol == last_symbol)\n     {\n      return last_point;\n     }\n\n//-- variant B) search in the array cache\n   int i       = last_i;\n   int start_i = i;\n   bool found  = false;\n\n   if(size > 0)\n     {\n      while(true)\n        {\n         if(symbols[i] == symbol)\n           {\n            last_symbol = symbol;\n            last_point  = points[i];\n            last_i      = i;\n\n            return last_point;\n           }\n\n         i++;\n\n         if(i >= size)\n           {\n            i = 0;\n           }\n         if(i == start_i)\n           {\n            break;\n           }\n        }\n     }\n\n//-- variant C) add this symbol to the cache\n   i     = size;\n   size  = size + 1;\n\n   ArrayResize(symbols, size);\n   ArrayResize(points, size);\n\n   symbols[i]  = symbol;\n   points[i]   = 0;\n   last_symbol = symbol;\n   last_i      = i;\n\n//-- unserialize rules from FXD_POINT_FORMAT_RULES\n   string rules[];\n   StringExplode(\",\", POINT_FORMAT_RULES, rules);\n\n   int rules_count = ArraySize(rules);\n\n   if(rules_count > 0)\n     {\n      string rule[];\n\n      for(int r = 0; r < rules_count; r++)\n        {\n         StringExplode(\"=\", rules[r], rule);\n\n         //-- a single rule must contain 2 parts, [0] from and [1] to\n         if(ArraySize(rule) != 2)\n           {\n            continue;\n           }\n\n         double from = StringToDouble(rule[0]);\n         double to   = StringToDouble(rule[1]);\n\n         //-- \"to\" must be a positive number, different than 0\n         if(to <= 0)\n           {\n            continue;\n           }\n\n         //-- \"from\" can be a number or a string\n         // a) string\n         if(from == 0 && StringLen(rule[0]) > 0)\n           {\n            string s_from = rule[0];\n            int pos       = StringFind(s_from, \"?\");\n\n            if(pos < 0)  // ? not found\n              {\n               if(StringFind(symbol, s_from) == 0)\n                 {\n                  points[i] = to;\n                 }\n              }\n            else\n               if(pos == 0)  // ? is the first symbol => match the second symbol\n                 {\n                  if(StringFind(symbol, StringSubstr(s_from, 1), 3) == 3)\n                    {\n                     points[i] = to;\n                    }\n                 }\n               else\n                  if(pos > 0)  // ? is the second symbol => match the first symbol\n                    {\n                     if(StringFind(symbol, StringSubstr(s_from, 0, pos)) == 0)\n                       {\n                        points[i] = to;\n                       }\n                    }\n           }\n\n         // b) number\n         if(from == 0)\n           {\n            continue;\n           }\n\n         if(SymbolInfoDouble(symbol, SYMBOL_POINT) == from)\n           {\n            points[i] = to;\n           }\n        }\n     }\n\n   if(points[i] == 0)\n     {\n      points[i] = SymbolInfoDouble(symbol, SYMBOL_POINT);\n     }\n\n   last_point = points[i];\n\n   return last_point;\n  }\n\n"
    return result


def get_fun__string_explode():
    result = "template<typename T>\nvoid StringExplode(string delimiter, string inputString, T &output[])\n  {\n   int begin   = 0;\n   int end     = 0;\n   int element = 0;\n   int length  = StringLen(inputString);\n   int length_delimiter = StringLen(delimiter);\n   T empty_val  = (typename(T) == \"string\") ? (T)\"\" : (T)0;\n\n   if(length > 0)\n     {\n      while(true)\n        {\n         end = StringFind(inputString, delimiter, begin);\n\n         ArrayResize(output, element + 1);\n         output[element] = empty_val;\n\n         if(end != -1)\n           {\n            if(end > begin)\n              {\n               output[element] = (T)StringSubstr(inputString, begin, end - begin);\n              }\n           }\n         else\n           {\n            output[element] = (T)StringSubstr(inputString, begin, length - begin);\n            break;\n           }\n\n         begin = end + 1 + (length_delimiter - 1);\n         element++;\n        }\n     }\n   else\n     {\n      ArrayResize(output, 1);\n      output[element] = empty_val;\n     }\n  }\n"
    return result


def get_fun__to_digits():
    result = "double toDigits(double pips, string symbol)\n  {\n   if(symbol == \"\")\n      symbol = Symbol();\n\n   int digits   = (int)SymbolInfoInteger(symbol, SYMBOL_DIGITS);\n   double point = SymbolInfoDouble(symbol, SYMBOL_POINT);\n\n   return NormalizeDouble(pips * PipValue(symbol) * point, digits);\n  }\n"
    return result


def get_fun__string_trim():
    result = "string StringTrim(string str)\n  {\n   str = StringTrimRight(str);\n   str = StringTrimLeft(str);\n\n   return str;\n  }\n"
    return result


def get_fun__format_value_for_printing_all():
    result = "\ntemplate<typename T>\nstring FormatValueForPrinting(T value, int digits, int timeFormat)\n  {\n   string outputValue = \"\";\n   string typeName    = typename(value);\n\n   if(typeName == \"double\" || typeName == \"float\")\n     {\n      if(digits >= -16 && digits <= 8)\n        {\n         if(value > -1.0 && value < 1.0)\n           {\n            /**\n            * Find how many zeroes are after the point, but before the first non-zero digit.\n            * For example 0.000195 has 3 zeroes\n            * The function would return negative value for values bigger than 0\n            *\n            * @see https://stackoverflow.com/questions/31001901/how-can-i-count-the-number-of-zero-decimals-in-javascript/31002148#31002148\n            */\n            int zeroesAfterPoint = (int)-MathFloor(MathLog10(MathAbs(value)) + 1);\n\n            digits = zeroesAfterPoint + digits;\n           }\n\n         T normalizedValue  = NormalizeDouble(value, digits);\n         outputValue = DoubleToString(normalizedValue, digits);\n        }\n      else\n        {\n         outputValue = (string)NormalizeDouble(value, 8);\n        }\n     }\n   else\n     {\n      outputValue = IntegerToString((long)value);\n     }\n\n   return outputValue;\n  }\n\n\n\n\n/**\n* Bool overload\n*/\nstring FormatValueForPrinting(\n   bool value,\n   int digits,\n   int timeFormat\n)\n  {\n   return (value) ? \"true\" : \"false\";\n  }\n\n/**\n* Datetime overload\n*/\nstring FormatValueForPrinting(\n   datetime value,\n   int digits,\n   int timeFormat\n)\n  {\n   if(timeFormat == (int)EMPTY_VALUE || timeFormat == EMPTY_VALUE)\n      timeFormat = TIME_DATE|TIME_MINUTES;\n   return TimeToString(value, timeFormat);\n  }\n\n/**\n* String overload\n*/\nstring FormatValueForPrinting(\n   string value,\n   int digits,\n   int timeFormat\n)\n  {\n   return value;\n  }\n"
    return result


def get_fun__window_find_visible():
    result = "int WindowFindVisible(long chart_id, string term)\n  {\n//-- the search term can be chart name, such as Force(13), or subwindow index\n   if(term == \"\" || term == \"0\")\n     {\n      return 0;\n     }\n\n   int subwindow = (int)StringToInteger(term);\n\n   if(subwindow == 0 && StringLen(term) > 1)\n     {\n      subwindow = ChartWindowFind(chart_id, term);\n     }\n\n   if(subwindow > 0 && !ChartGetInteger(chart_id, CHART_WINDOW_IS_VISIBLE, subwindow))\n     {\n      return -1;\n     }\n\n   return subwindow;\n  }\n"
    return result


def get_fun__symbol_ask():
    result = "double SymbolAsk(string symbol)\n  {\n   if(symbol == \"\")\n      symbol = Symbol();\n\n   return SymbolInfoDouble(symbol, SYMBOL_ASK);\n  }"
    return result


def get_fun__symbol_bid():
    result = "double SymbolBid(string symbol)\n  {\n   if(symbol == \"\")\n      symbol = Symbol();\n\n   return SymbolInfoDouble(symbol, SYMBOL_BID);\n  }"
    return result


def get_fun__is_order_type_buy():
    result = "bool IsOrderTypeBuy()\n  {\n   int type = OrderType();\n\n   return (type == OP_BUY || type == OP_BUYSTOP || type == OP_BUYLIMIT);\n  }"
    return result


def get_fun__is_order_type_stop():
    result = "bool IsOrderTypeStop()\n  {\n   int type = OrderType();\n\n   return (type == OP_BUYSTOP || type == OP_SELLSTOP);\n  }"
    return result


def get_fun__get_symbol():
    result = "string getSymbol(string symbol)\n  {\n   return (symbol==NULL || symbol==\"\") && overriding_symbol != \"\" ? overriding_symbol : symbol;\n  }"
    return result


def get_fun__get_timeframe():
    result = "int getTimeframe(int timeframe)\n  {\n   return timeframe==PERIOD_CURRENT && overriding_timeframe != -1 ? overriding_timeframe : timeframe;\n  }\n"
    return result


def get_fun__is_symbol_accepted():
    result = "bool is_symbol_accepted(int symbol_mode, string &symbols[])\n  {\n   if(symbol_mode == SYMBOL_MODE_ANY)\n     {\n      return true;\n     }\n   else\n      if(ArraySize(symbols)==0)\n        {\n         bool case_1 = OrderSymbol() == getSymbol(\"\");\n         bool case_2 = OrderSymbol() == Symbol() && getSymbol(\"\")==\"\";\n         return case_1 || case_2;   \n        }\n      else\n        {\n         for(int i=ArraySize(symbols)-1; i>=0; i--)\n           {\n            string smb = StringTrimRight(symbols[i]);\n            smb = StringTrimLeft(smb);\n            if(smb==OrderSymbol())\n              {\n               return true;\n              }\n           }\n        }\n   return false;\n  }"
    return result


def get_fun__load_object():
    result = "bool load_object(int index, long chart_id,int sub_window, int obj_type)\n  {\n   string name = ObjectName(chart_id,index,sub_window, obj_type);\n\n   if(name == \"\")\n     {\n      return false;\n     }\n\n   loaded_object_chart_id(chart_id);\n   loaded_object_name(name);\n   loaded_object_subwindow(sub_window);\n   loaded_object_type((int)ObjectGetInteger(chart_id,name,OBJPROP_TYPE));\n\n   return true;\n  }\n"
    return result


def get_fun__loaded_object_chart_id():
    result = "long loaded_object_chart_id(long chart_id=-1) {static long memory=-1; if(chart_id>-1) {memory=chart_id;} return(memory);}\n"
    return result


def get_fun__loaded_object_name():
    result = "string loaded_object_name(string name=\"\") {static string memory=\"\"; if(name!=\"\") {memory=name;} return(memory);}\n"
    return result


def get_fun__loaded_object_subwindow():
    result = "int loaded_object_subwindow(int sub_window=-2) {static int memory=-2; if(sub_window>-2) {memory=sub_window;} return(memory);}\n"
    return result


def get_fun__loaded_object_type():
    result = "int loaded_object_type(int type=-2) {static int memory=-2; if(type>-2) {memory=type;} return(memory);}\n"
    return result


def get_fun__array_ensure_value():
    result = "template<typename T>\nbool array_ensure_value(T &array[], T value)\n  {\n   int size   = ArraySize(array);\n\n   if(size > 0)\n     {\n      if(in_array(array, value))\n        {\n         // value found -> exit\n         return false; // no value added\n        }\n     }\n\n// value does not exists -> add it\n   ArrayResize(array, size+1);\n   array[size] = value;\n\n   return true; // value added\n  }\n"
    return result


def get_fun__in_array():
    result = "template<typename T>\nbool in_array(T &array[], T value)\n  {\n   int size = ArraySize(array);\n\n   if(size > 0)\n     {\n      for(int i = 0; i < size; i++)\n        {\n         if(array[i] == value)\n           {\n            return true;\n           }\n        }\n     }\n\n   return false;\n  }\n"
    return result
