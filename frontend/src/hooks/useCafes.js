import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { fetchCafes, addCafe, updateCafe, deleteCafe } from '../api';

export const useCafes = (location) => {
    const queryClient = useQueryClient();

    const cafesQuery = useQuery({
        queryKey: ["cafes", location],
        queryFn: fetchCafes,
    });

    const addCafeMutation = useMutation({
        mutationFn: addCafe,
        onSuccess: () => {
            queryClient.invalidateQueries(['cafes']);
        },
    });

    const updateCafeMutation = useMutation({
        mutationFn: updateCafe,
        onSuccess: () => {
            queryClient.invalidateQueries(['cafes']);
        },
    });

    const deleteCafeMutation = useMutation({
        mutationFn: deleteCafe,
        onSuccess: () => {
            queryClient.invalidateQueries(['cafes']);
        },
    });

    return {
        cafesQuery,
        addCafeMutation,
        updateCafeMutation,
        deleteCafeMutation,
    };
};