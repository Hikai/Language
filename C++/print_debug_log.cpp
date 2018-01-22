#include <stdio.h>

void log_debug(const char *format, ...)
{
	char str[1024];
	va_list var_arg;

	va_start(var_arg, format);
	_vsnprintf_s(str, 1024, format, var_arg);
	va_end(var_arg);
	OutputDebugStringA(str);

	return;
}

int main(void)
{
	log_debug("asdf %d", 1234);
	
	return 0;
}
