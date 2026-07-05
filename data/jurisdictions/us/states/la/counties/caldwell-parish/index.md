---
type: Jurisdiction
title: "Caldwell Parish, LA"
classification: county
fips: "22021"
state: "LA"
demographics:
  population: 9500
  population_under_18: 2134
  population_18_64: 5609
  population_65_plus: 1757
  median_household_income: 47028
  poverty_rate: 29.78
  homeownership_rate: 68.92
  unemployment_rate: 10.06
  median_home_value: 93300
  gini_index: 0.4894
  vacancy_rate: 20.38
  race_white: 7177
  race_black: 1836
  race_asian: 0
  race_native: 1
  hispanic: 111
  bachelors_plus: 995
districts:
  - to: "us/states/la/districts/05"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/la/districts/senate/32"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/la/districts/house/20"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Caldwell Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9500 |
| Under 18 | 2134 |
| 18–64 | 5609 |
| 65+ | 1757 |
| Median household income | 47028 |
| Poverty rate | 29.78 |
| Homeownership rate | 68.92 |
| Unemployment rate | 10.06 |
| Median home value | 93300 |
| Gini index | 0.4894 |
| Vacancy rate | 20.38 |
| White | 7177 |
| Black | 1836 |
| Asian | 0 |
| Native | 1 |
| Hispanic/Latino | 111 |
| Bachelor's or higher | 995 |

## Districts

- [LA-05](/us/states/la/districts/05.md) — 100% (congressional)
- [LA Senate District 32](/us/states/la/districts/senate/32.md) — 100% (state senate)
- [LA House District 20](/us/states/la/districts/house/20.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
