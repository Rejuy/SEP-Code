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
      .post(global.config.backendUrl + "/api/admin/activate_user", {
        id: params.row.id,
      })
      .then((res) => {
        if (res.data.state === "found") {
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
          Would You Like to Activate User "{params.row.username}"?
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
    axios.get(global.config.backendUrl + "/api/admin/get_users").then((res) => {
      setData(res.data.users);
    });
  }, []);
  const columns = [
    { field: "id", headerName: "ID", width: 70 },
    {
      field: "account",
      headerName: "Account",
      headerAlign: "center",
      width: 160,
      renderCell: (params) => {
        var user_icon_element, user_icon_url;
        if ((user_icon_url = params.row.user_icon)) {
          user_icon_element = (
            <img
              src={user_icon_url}
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
            {params.row.username}
          </div>
        );
      },
    },
    {
      field: "activated",
      headerName: "Account Active",
      headerAlign: "center",
      width: 200,
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
      />
    </CustomContainer>
  );
}

export default Userpage;
