# -*- coding: utf-8 -*-
import os

def get_subdir_list( dirpath ):
	dirpath = str( dirpath )
	if dirpath=="":
		return []
	dirpath = dirpath.replace( "/","\\")
	if dirpath[ -1] != "\\":
		dirpath = dirpath+"\\"
	a = os.listdir( dirpath )
	return [ x for x in a if os.path.isdir( dirpath + x ) ]

def get_file_list( dirpath ):
	dirpath = str( dirpath )
	if dirpath=="":
		return []
	dirpath = dirpath.replace( "/","\\")
	if dirpath[ -1] != "\\":
		dirpath = dirpath+"\\"
	a = os.listdir( dirpath )
	return [ x for x in a if (not os.path.isdir( dirpath + x )) ]