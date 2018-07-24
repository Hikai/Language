LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_SRC_FILES := \
	x5.c

LOCAL_MODULE := test.c
LOCAL_LDFLAGS   += -llog
LOCAL_CFLAGS    += -DDEBUG

include $(BUILD_EXECUTABLE)
