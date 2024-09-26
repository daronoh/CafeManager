import React, { useState } from 'react';
import { useEmployees } from '../hooks/useEmployees';
import EmployeeTable from '../components/EmployeeTable';
import { Button, CircularProgress, Dialog, DialogActions, DialogContent, DialogTitle, Snackbar } from '@mui/material';
import EmployeeForm from '../components/EmployeeForm';
import { useParams } from '@tanstack/react-router';
import { useCafes } from '../hooks/useCafes';

const EmployeesPage = () => {
    const { cafeName } = useParams({ strict: false });
    const { cafesQuery } = useCafes();
    const { data: cafes } = cafesQuery;
    const { employeesQuery, addEmployeeMutation, updateEmployeeMutation, deleteEmployeeMutation } = useEmployees(cafeName);
    const [open, setOpen] = useState(false);
    const [initialData, setInitialData] = useState(null);
    const [hasUnsavedChanges, setHasUnsavedChanges] = useState(false);
    const { data: employees, isLoading, isError, error } = employeesQuery;

    const handleAddEmployee = () => {
        setInitialData(null);
        setOpen(true);
    };

    const handleEditEmployee = (employee) => {
        setInitialData(employee);
        setOpen(true);
    }

    const handleCancel = () => {
        if (hasUnsavedChanges) {
            if (!window.confirm('You have unsaved changes. Are you sure you want to leave?')) {
                return;
            }
        }
        handleClose();
    };

    const handleClose = () => {
        setOpen(false);
        setInitialData(null);
        setHasUnsavedChanges(false);
    }

    const handleDeleteEmployee = (id) => {
        if (window.confirm('Are you sure you want to delete this employee?')) {
            deleteEmployeeMutation.mutate(id);
        }
    };

    const handleDataChange = (data) => {
        setHasUnsavedChanges(data !== initialData);
    };

    const onSubmit = async (data) => {
        try {
            if (initialData) {
                await updateEmployeeMutation.mutateAsync({ employeeId: initialData.id, employeeData: data });
            } else {
                await addEmployeeMutation.mutateAsync(data);
            }
            handleClose();
        } catch (error) {
            if (error.response && error.response.status === 422) {
                alert(`Error: Invalid details provided.`);
            } else {
                alert(`Error: ${error.message || 'An error occurred'}`);
            }
        }
    };

    if (isLoading) return <CircularProgress />;
    if (isError) return <Snackbar message={`Error: ${error.message}`} open={true} />;

    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', margin: '20px' }}>
            <Button 
                onClick={handleAddEmployee} 
                variant="contained" 
                style={{ marginBottom: '20px', backgroundColor: '#4CAF50', color: 'white', fontWeight: 'bold' }}
            >
                Add New Employee
            </Button>
            
            <EmployeeTable employees={employees} onEdit={handleEditEmployee} onDelete={handleDeleteEmployee} />
            
            <Dialog open={open} onClose={handleCancel}>
                <DialogTitle>{initialData ? 'Edit Employee' : 'Add New Employee'}</DialogTitle>
                <DialogContent>
                    <EmployeeForm onSubmit={onSubmit} initialData={initialData} onDataChange={handleDataChange} cafes = {cafes}/>
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleCancel} color="primary">Cancel</Button>
                </DialogActions>
            </Dialog>
        </div>
    );
};

export default EmployeesPage;