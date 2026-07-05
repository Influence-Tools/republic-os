---
type: Jurisdiction
title: "Orleans County, NY"
classification: county
fips: "36073"
state: "NY"
demographics:
  population: 39608
  population_under_18: 7433
  population_18_64: 24308
  population_65_plus: 7867
  median_household_income: 65969
  poverty_rate: 12.75
  homeownership_rate: 77.16
  unemployment_rate: 5.09
  median_home_value: 140800
  gini_index: 0.4274
  vacancy_rate: 11.49
  race_white: 34032
  race_black: 1944
  race_asian: 303
  race_native: 167
  hispanic: 2165
  bachelors_plus: 7491
districts:
  - to: "us/states/ny/districts/24"
    rel: in-district
    area_weight: 0.4794
  - to: "us/states/ny/districts/senate/62"
    rel: in-district
    area_weight: 0.4796
  - to: "us/states/ny/districts/house/139"
    rel: in-district
    area_weight: 0.4796
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Orleans County, NY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39608 |
| Under 18 | 7433 |
| 18–64 | 24308 |
| 65+ | 7867 |
| Median household income | 65969 |
| Poverty rate | 12.75 |
| Homeownership rate | 77.16 |
| Unemployment rate | 5.09 |
| Median home value | 140800 |
| Gini index | 0.4274 |
| Vacancy rate | 11.49 |
| White | 34032 |
| Black | 1944 |
| Asian | 303 |
| Native | 167 |
| Hispanic/Latino | 2165 |
| Bachelor's or higher | 7491 |

## Districts

- [NY-24](/us/states/ny/districts/24.md) — 48% (congressional)
- [NY Senate District 62](/us/states/ny/districts/senate/62.md) — 48% (state senate)
- [NY House District 139](/us/states/ny/districts/house/139.md) — 48% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
