---
type: Jurisdiction
title: "Catawba County, NC"
classification: county
fips: "37035"
state: "NC"
demographics:
  population: 163573
  population_under_18: 35394
  population_18_64: 97568
  population_65_plus: 30611
  median_household_income: 67864
  poverty_rate: 12.74
  homeownership_rate: 72.17
  unemployment_rate: 3.66
  median_home_value: 241600
  gini_index: 0.4589
  vacancy_rate: 9.44
  race_white: 122021
  race_black: 12945
  race_asian: 6962
  race_native: 944
  hispanic: 18786
  bachelors_plus: 38651
districts:
  - to: "us/states/nc/districts/10"
    rel: in-district
    area_weight: 0.9987
  - to: "us/states/nc/districts/senate/45"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nc/districts/house/89"
    rel: in-district
    area_weight: 0.7142
  - to: "us/states/nc/districts/house/96"
    rel: in-district
    area_weight: 0.2855
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Catawba County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 163573 |
| Under 18 | 35394 |
| 18–64 | 97568 |
| 65+ | 30611 |
| Median household income | 67864 |
| Poverty rate | 12.74 |
| Homeownership rate | 72.17 |
| Unemployment rate | 3.66 |
| Median home value | 241600 |
| Gini index | 0.4589 |
| Vacancy rate | 9.44 |
| White | 122021 |
| Black | 12945 |
| Asian | 6962 |
| Native | 944 |
| Hispanic/Latino | 18786 |
| Bachelor's or higher | 38651 |

## Districts

- [NC-10](/us/states/nc/districts/10.md) — 100% (congressional)
- [NC Senate District 45](/us/states/nc/districts/senate/45.md) — 100% (state senate)
- [NC House District 89](/us/states/nc/districts/house/89.md) — 71% (state house)
- [NC House District 96](/us/states/nc/districts/house/96.md) — 29% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
