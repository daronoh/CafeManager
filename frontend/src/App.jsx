import React from 'react';
import {Outlet, RouterProvider, createRootRoute, createRoute, createRouter } from '@tanstack/react-router';
import CafesPage from './pages/CafesPage';
import EmployeesPage from './pages/EmployeesPage';
import Banner from './components/Banner';
import HomePage from './pages/HomePage';

const rootRoute = createRootRoute({
    component: () => (
        <>
        <Banner />
        <Outlet />
        </>
    )
})

const homeRoute = createRoute({
    getParentRoute: () => rootRoute,
    path: '/',
    component: HomePage,
});

const cafeRoute = createRoute({
    getParentRoute: () => rootRoute,
    path: `/cafes`,
    component: CafesPage,
});

const employeeRoute = createRoute({
    getParentRoute: () => rootRoute,
    path: '/employees',
    component: EmployeesPage, 
});

const employeeUnderCafeRoute = createRoute({
    getParentRoute: () => rootRoute,
    path: '/employees/$cafeName',
    component: EmployeesPage,
})

const routeTree = rootRoute.addChildren([homeRoute, employeeRoute, cafeRoute, employeeUnderCafeRoute])

const router = createRouter({ routeTree })

const App = () => {
    return (
        <RouterProvider router={router} />
    );
};

export default App;