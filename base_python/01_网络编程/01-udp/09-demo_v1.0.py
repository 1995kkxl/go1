pdate ${DIR_SRC_DEV}
    a_rev_src_dev=$(F_GET_SVN_REVISION ${DIR_SRC_DEV})
else
    svn update -r ${a_rev_src_dev} ${DIR_SRC_DEV}
fi
F_LOG_EXIT " 同步源码 更新目录 DIR_SRC_DEV ${a_rev_src_dev} " ${log_file}

if [[ -z "${a_rev_src_ops}" ]]; then
    svn update ${DIR_SRC_OPS}
    a_rev_src_ops=$(F_GET_SVN_REVISION ${DIR_SRC_OPS})
else
    svn update ${DIR_SRC_OPS} && \
    cd ${DIR_SRC_OPS} && \
    svn merge -r HEAD:${a_rev_src_ops} ${DIR_SRC_OPS} && \
    cd -
fi
F_LOG_EXIT " 同步源码 更新目录 DIR_SRC_OPS ${a_rev_src_ops} " ${log_file}

## 同步源码
if [[ -z "${a_fix_src_dev}" ]]; then
    rsync -acv --delete --exclude=".svn" ${DIR_SRC_DEV}/ ${DIR_SRC_OPS}/
    F_LOG_EXIT " 同步源码 DIR_SRC_DEV:${a_rev_src_dev} -> DIR_SRC_OPS:${a_rev_src_ops} " ${log_file}
else
    file_list=($(cat