---
type: Jurisdiction
title: "Jackson County, NC"
classification: county
fips: "37099"
state: "NC"
demographics:
  population: 43771
  population_under_18: 7164
  population_18_64: 27760
  population_65_plus: 8847
  median_household_income: 55815
  poverty_rate: 18.01
  homeownership_rate: 60.78
  unemployment_rate: 4.91
  median_home_value: 284700
  gini_index: 0.4878
  vacancy_rate: 33.71
  race_white: 34741
  race_black: 982
  race_asian: 446
  race_native: 2907
  hispanic: 3500
  bachelors_plus: 12517
districts:
  - to: "us/states/nc/districts/11"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nc/districts/senate/50"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nc/districts/house/119"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Jackson County, NC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43771 |
| Under 18 | 7164 |
| 18–64 | 27760 |
| 65+ | 8847 |
| Median household income | 55815 |
| Poverty rate | 18.01 |
| Homeownership rate | 60.78 |
| Unemployment rate | 4.91 |
| Median home value | 284700 |
| Gini index | 0.4878 |
| Vacancy rate | 33.71 |
| White | 34741 |
| Black | 982 |
| Asian | 446 |
| Native | 2907 |
| Hispanic/Latino | 3500 |
| Bachelor's or higher | 12517 |

## Districts

- [NC-11](/us/states/nc/districts/11.md) — 100% (congressional)
- [NC Senate District 50](/us/states/nc/districts/senate/50.md) — 100% (state senate)
- [NC House District 119](/us/states/nc/districts/house/119.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
