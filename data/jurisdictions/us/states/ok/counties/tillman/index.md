---
type: Jurisdiction
title: "Tillman County, OK"
classification: county
fips: "40141"
state: "OK"
demographics:
  population: 6910
  population_under_18: 1645
  population_18_64: 3864
  population_65_plus: 1401
  median_household_income: 48939
  poverty_rate: 21.01
  homeownership_rate: 72.75
  unemployment_rate: 5.87
  median_home_value: 79800
  gini_index: 0.4774
  vacancy_rate: 28.82
  race_white: 4462
  race_black: 490
  race_asian: 19
  race_native: 148
  hispanic: 1919
  bachelors_plus: 1002
districts:
  - to: "us/states/ok/districts/04"
    rel: in-district
    area_weight: 0.9974
  - to: "us/states/ok/districts/senate/38"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/ok/districts/house/63"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Tillman County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6910 |
| Under 18 | 1645 |
| 18–64 | 3864 |
| 65+ | 1401 |
| Median household income | 48939 |
| Poverty rate | 21.01 |
| Homeownership rate | 72.75 |
| Unemployment rate | 5.87 |
| Median home value | 79800 |
| Gini index | 0.4774 |
| Vacancy rate | 28.82 |
| White | 4462 |
| Black | 490 |
| Asian | 19 |
| Native | 148 |
| Hispanic/Latino | 1919 |
| Bachelor's or higher | 1002 |

## Districts

- [OK-04](/us/states/ok/districts/04.md) — 100% (congressional)
- [OK Senate District 38](/us/states/ok/districts/senate/38.md) — 100% (state senate)
- [OK House District 63](/us/states/ok/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
