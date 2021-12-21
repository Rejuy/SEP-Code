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
        <DialogTitle>Activate User</DialogTitle>
        <DialogContent>
          Would You Like to Activate User "{params.row.user_name}"?
        </DialogContent>
        <DialogActions>
          <Button
            onClick={() => {
              setOpen(false);
            }}
            variant="outlined"
            color="error"
          >
            No
          </Button>
          <Button
            onClick={() => {
              setOpen(false);
              activateUser();
            }}
            variant="outlined"
            color="success"
          >
            Yes
          </Button>
        </DialogActions>
      </Dialog>
      <Link to={"/user/" + params.row.id} style={{ marginRight: "10px" }}>
        <Button variant="outlined">Edit</Button>
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
          Activate
        </Button>
      )}
    </>
  );
}

function Userpage() {
  const [data, setData] = useState([]);
  useEffect(() => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/admin_get_users", {
        secret_code: localStorage.getItem("secretCode"),
        offset: 0,
        size: 1000,
      })
      .then((res) => {
        setData(res.data.users.sort((a, b) => a.id - b.id));
      });
  }, []);
  const columns = [
    { field: "id", headerName: "ID", width: 70 },
    {
      field: "user_name",
      headerName: "Username",
      headerAlign: "center",
      width: 160,
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
      headerName: "Email",
      headerAlign: "center",
      align: "center",
      width: 125,
    },
    {
      field: "account_birth",
      headerName: "Account Birth",
      headerAlign: "center",
      align: "center",
      type: "date",
      width: 125,
      valueFormatter: (params) => {
        return new Date(params.value).toLocaleDateString("zh-Hans-CN");
      },
    },
    {
      field: "collection_count",
      headerName: "Collection Count",
      headerAlign: "center",
      align: "center",
      width: 100,
    },
    {
      field: "like_count",
      headerName: "Like Count",
      headerAlign: "center",
      align: "center",
      width: 100,
    },
    {
      field: "comment_count",
      headerName: "Comment Count",
      headerAlign: "center",
      align: "center",
      width: 100,
    },
    {
      field: "item_count",
      headerName: "Item Count",
      headerAlign: "center",
      align: "center",
      width: 100,
    },
    {
      field: "activated",
      headerName: "Account Active",
      headerAlign: "center",
      width: 125,
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
      headerName: "Actions",
      headerAlign: "center",
      sortable: false,
      width: 300,
      renderCell: ActionInit,
    },
  ];
  return (
    <CustomContainer>
      <Typography variant="h5" style={{ marginBottom: "20px" }}>
        Users
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
    </CustomContainer>
  );
}

export default Userpage;
