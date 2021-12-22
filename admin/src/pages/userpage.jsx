import { AccountBox, Check, Close } from "@mui/icons-material";
import {
  styled,
  Container,
  Typography,
  Button,
  Dialog,
  DialogTitle,
  DialogActions,
  DialogContent,
  CircularProgress,
} from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "../config";

const CustomContainer = styled(Container)(({ theme }) => ({
  paddingTop: theme.spacing(12),
  height: theme.spacing(75),
  width: "100%",
}));

function ActionInit(params) {
  const [open, setOpen] = useState(false);

  const handleDialogClose = () => {
    setOpen(false);
  };

  const jsonDetail = (e) => {
    e.stopPropagation();

    const api = params.api;
    const thisRow = {};

    api
      .getAllColumns()
      .filter((c) => c.field !== "__check__" && !!c)
      .forEach((c) => (thisRow[c.field] = params.getValue(params.id, c.field)));

    return alert(JSON.stringify(thisRow, null, 4));
  };

  const activateUser = () => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/admin_edit_user", {
        secret_code: localStorage.getItem("secretCode"),
        user: { ...params.row, activated: 1 },
        delete: false,
      })
      .then((res) => {
        if (res.data.status === 0) {
          params.row.activated = true;
          params.api.forceUpdate();
        }
      });
  };

  return (
    <>
      <Dialog open={open} onClose={handleDialogClose}>
        <DialogTitle>激活</DialogTitle>
        <DialogContent>
          是否想要激活用户 "{params.row.user_name}"?
        </DialogContent>
        <DialogActions>
          <Button
            onClick={() => {
              setOpen(false);
            }}
            variant="outlined"
            color="error"
          >
            否
          </Button>
          <Button
            onClick={() => {
              setOpen(false);
              activateUser();
            }}
            variant="outlined"
            color="success"
          >
            是
          </Button>
        </DialogActions>
      </Dialog>
      <Link to={"/user/" + params.row.id} style={{ marginRight: "10px" }}>
        <Button variant="outlined">修改</Button>
      </Link>
      <Button
        onClick={jsonDetail}
        variant="outlined"
        style={{ marginRight: "10px" }}
      >
        JSON
      </Button>
      {params.row.activated ? null : (
        <Button
          variant="outlined"
          onClick={(e) => {
            e.stopPropagation();
            setOpen(true);
          }}
          color="success"
        >
          激活
        </Button>
      )}
    </>
  );
}

function Userpage() {
  const [data, setData] = useState([]);
  const [loaded, setLoaded] = useState(false);
  useEffect(() => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/admin_get_users", {
        secret_code: localStorage.getItem("secretCode"),
        offset: 0,
        size: 1000,
      })
      .then((res) => {
        setData(res.data.users.sort((a, b) => a.id - b.id));
        setLoaded(true);
      });
  }, []);
  const columns = [
    { field: "id", headerName: "ID", flex: 1 },
    {
      field: "user_name",
      headerName: "用户名",
      headerAlign: "center",
      flex: 4,
      renderCell: (params) => {
        var user_icon_element,
          user_icon_url = params.row.image;
        if (user_icon_url) {
          user_icon_element = (
            <img
              src={"http://thurec.xyz/" + user_icon_url}
              alt="User Icon"
              style={{
                width: "32px",
                height: "32px",
                borderRadius: "2px",
                marginRight: "10px",
                objectFit: "fill",
              }}
            />
          );
        } else {
          user_icon_element = (
            <AccountBox
              style={{
                width: "32px",
                height: "32px",
                marginRight: "10px",
              }}
            />
          );
        }
        return (
          <div
            className="account"
            style={{
              display: "flex",
              alignItems: "center",
              width: "100%",
            }}
          >
            {user_icon_element}
            {params.row.user_name}
          </div>
        );
      },
    },
    {
      field: "email",
      headerName: "邮箱",
      headerAlign: "center",
      align: "center",
      flex: 2,
    },
    {
      field: "account_birth",
      headerName: "帐号生日",
      headerAlign: "center",
      align: "center",
      type: "date",
      flex: 2,
      valueFormatter: (params) => {
        return new Date(params.value).toLocaleDateString("zh-Hans-CN");
      },
    },
    {
      field: "collection_count",
      headerName: "收藏个数",
      headerAlign: "center",
      align: "center",
      flex: 1,
    },
    {
      field: "like_count",
      headerName: "点赞个数",
      headerAlign: "center",
      align: "center",
      flex: 1,
    },
    {
      field: "comment_count",
      headerName: "评论个数",
      headerAlign: "center",
      align: "center",
      flex: 1,
    },
    {
      field: "item_count",
      headerName: "发帖个数",
      headerAlign: "center",
      align: "center",
      flex: 1,
    },
    {
      field: "activated",
      headerName: "激活",
      headerAlign: "center",
      flex: 1,
      renderCell: (params) => {
        if (params.value) {
          return <Check style={{ width: "100%" }} />;
        } else {
          return <Close style={{ width: "100%" }} />;
        }
      },
    },
    {
      field: "action",
      headerName: "操作",
      headerAlign: "center",
      sortable: false,
      flex: 8,
      renderCell: ActionInit,
    },
  ];

  const loadingJsx = (
    <div
      className="loading"
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "space-evenly",
      }}
    >
      <Typography variant="h5">Loading Users</Typography>
      <CircularProgress />
    </div>
  );

  const dataGridJsx = (
    <div style={{ width: "100%" }}>
      <Typography variant="h5" style={{ marginBottom: "20px" }}>
        用户
      </Typography>
      <DataGrid
        id="datagrid"
        rows={data}
        columns={columns}
        pageSize={8}
        rowsPerPageOptions={[8]}
        checkboxSelection
        autoHeight={true}
        style={{ width: "100%" }}
      />
    </div>
  );

  return (
    <CustomContainer
      style={{ display: "flex", justifyContent: "space-evenly" }}
    >
      {loaded ? dataGridJsx : loadingJsx}
    </CustomContainer>
  );
}

export default Userpage;
