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

def get_fun__time_from_string ():
  result = "//stamp is like: \"2023.04.15 18:25:40\"\ndatetime TimeFromString(int time_mode, string stamp)\n  {\n   datetime t = 0;\n\n   if(time_mode == TIME_SERVER)\n      t = TimeCurrent();\n   else\n      if(time_mode == TIME_LOCAL)\n         t = TimeLocal();\n      else\n         if(time_mode == TIME_GMT)\n            t = TimeGMT();\n\n   int stamplen = StringLen(stamp);\n\n   if(stamplen < 9)\n     {\n      int thour    = TimeHour(t);\n      int tminute  = TimeMinute(t);\n      int tseconds = TimeSeconds(t);\n\n      int hour   = (int)StringSubstr(stamp, 0, 2);\n      int minute = (int)StringSubstr(stamp, 3, 2);\n      int second = (int)StringSubstr(stamp, 6, 2);\n\n      datetime t1 = (datetime)(t - (thour-hour)*3600 - (tminute - minute)*60 - (tseconds-second));\n\n      return t1;\n     }\n\n   return StringToTime(stamp);\n  }\n"
  return result

def get_fun__get_group_number ():
  result = "//Considering each magic number is a 7 digit number like 2088100,\n//I choose to take first two digits as group number.\nint getGroupNumber (int magic){\n   return (int)(magic/1000000);\n}"
  return result

def get_fun__same_order_type ():
  result = "//This just checks if order is buy or sell\nbool sameOrderType (int type[], int orderType){\n   for (int i=0; i<ArraySize(type); i++)\n      if (orderType==type[i])\n         return true;\n   return false;\n}"
  return result

def get_fun__is_automated ():
  result = "//72 is the number in magic 3rd and 4th\n//digits that show it is opened by the expert\nbool isAutomated (int magic){\n   return MathMod((int)(magic/1000), 1000) == 72;\n}\n"
  return result

def get_fun__reverse_list ():
    result = "void ReverseList(int &arr[])\n  {\n   int size = ArraySize(arr);\n   ArraySetAsSeries(arr, true);\n\n   for(int i = 0; i < size / 2; i++)\n     {\n      int temp = arr[i];\n      arr[i] = arr[size - 1 - i];\n      arr[size - 1 - i] = temp;\n     }\n  }\n"
    return result

def get_fun__sleepex ():
    result = "#import \"kernel32.dll\"\nbool SleepEx(int ms, bool bAlertable);\n#import\n\n"
    return result
