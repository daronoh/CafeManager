import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { fetchEmployees, addEmployee, updateEmployee, deleteEmployee } from '../api';

export const useEmployees = (cafeName) => {
    const queryClient = useQueryClient();
    
    const employeesQuery = useQuery({
        queryKey: ["employees", cafeName],
        queryFn: fetchEmployees,
    });

    const addEmployeeMutation = useMutation({
        mutationFn: addEmployee,
        onSuccess: () => {
            queryClient.invalidateQueries(['employees', cafeName]);
        },
    });

    const updateEmployeeMutation = useMutation({
        mutationFn: updateEmployee,
        onSuccess: () => {
            queryClient.invalidateQueries(['employees', cafeName]);
        },
    });

    const deleteEmployeeMutation = useMutation({
        mutationFn: deleteEmployee,
        onSuccess: () => {
            queryClient.invalidateQueries(['employees', cafeName]);
        },
    });

    return {
        employeesQuery,
        addEmployeeMutation,
        updateEmployeeMutation,
        deleteEmployeeMutation,
    };
};