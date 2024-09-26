import React from 'react';
import { AgGridReact } from 'ag-grid-react';
import { Button } from '@mui/material';

const EmployeeTable = ({ employees, onEdit, onDelete }) => {
    const columnDefs = [
        { field: 'id', headerName: 'Employee ID', suppressHeaderMenuButton: true },
        { field: 'name', headerName: 'Name', suppressHeaderMenuButton: true },
        { field: 'email_address', headerName: 'Email Address', suppressHeaderMenuButton: true },
        { field: 'phone_number', headerName: 'Phone Number', suppressHeaderMenuButton: true },
        { field: 'days_worked', headerName: 'Days worked', suppressHeaderMenuButton: true },
        { field: 'cafe_name', headerName: 'Cafe name', suppressHeaderMenuButton: true },
        {
            field: 'actions',
            cellRenderer: (params) => (
                <>
                    <Button onClick={() => onEdit(params.data)}>Edit</Button>
                    <Button onClick={() => onDelete(params.data.id)}>Delete</Button>
                </>
            ),
            suppressHeaderMenuButton: true
        },
    ];

    return (
        <div className="ag-theme-alpine" style={{ height: 800, width: '100%' }}>
            <AgGridReact
                rowData={employees}
                columnDefs={columnDefs}
                pagination={true}
                paginationPageSize={20}
            />
        </div>
    );
};

export default EmployeeTable;