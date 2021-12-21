import { Check, Close } from "@mui/icons-material";
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

  const verifyItem = () => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/admin_activate_item", {
        secret_code: localStorage.getItem("secretCode"),
        class: 1,
        id: params.row.id,
      })
      .then((res) => {
        if (res.data.state === 0) {
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
          Would You Like to Verify Course "{params.row.name}"?
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
              verifyItem();
            }}
            variant="outlined"
            color="success"
          >
            Yes
          </Button>
        </DialogActions>
      </Dialog>
      <Link to={"/course/" + params.row.id} style={{ marginRight: "10px" }}>
        <Button variant="outlined">Edit</Button>
      </Link>
      <Button
        onClick={jsonDetail}
        variant="outlined"
        style={{ marginRight: "10px" }}
      >
        JSON
      </Button>
      {params.row.activated === 1 ? null : (
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

function Coursepage() {
  const [data, setData] = useState([]);
  useEffect(() => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/admin_get_item_list", {
        secret_code: localStorage.getItem("secretCode"),
        offset: 0,
        size: 99999,
        class: 1,
        order: 0,
      })
      .then((res) => {
        setData(res.data.items.sort((a, b) => a.id - b.id));
      });
  }, []);
  const columns = [
    { field: "id", headerName: "ID", width: 70 },
    {
      field: "name",
      headerName: "Course Name",
      headerAlign: "center",
      width: 160,
    },
    {
      field: "teacher",
      headerName: "Teacher",
      headerAlign: "center",
      align: "center",
      width: 125,
    },
    {
      field: "department",
      headerName: "Department",
      headerAlign: "center",
      align: "center",
      width: 125,
    },
    {
      field: "type",
      headerName: "Type",
      headerAlign: "center",
      align: "center",
      width: 125,
    },
    {
      field: "credit",
      headerName: "Credit",
      headerAlign: "center",
      align: "center",
      width: 125,
    },
    {
      field: "time",
      headerName: "Time",
      headerAlign: "center",
      align: "center",
      width: 125,
      valueFormatter: (params) => {
        return new Date(params.value).toLocaleDateString("zh-Hans-CN");
      },
    },
    {
      field: "activated",
      headerName: "Activated",
      headerAlign: "center",
      width: 125,
      renderCell: (params) => {
        if (params.value === 1) {
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
        Course
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

export default Coursepage;
