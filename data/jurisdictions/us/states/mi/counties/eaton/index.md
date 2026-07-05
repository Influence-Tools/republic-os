---
type: Jurisdiction
title: "Eaton County, MI"
classification: county
fips: "26045"
state: "MI"
demographics:
  population: 109130
  population_under_18: 22348
  population_18_64: 64842
  population_65_plus: 21940
  median_household_income: 79597
  poverty_rate: 8.33
  homeownership_rate: 74.17
  unemployment_rate: 4.53
  median_home_value: 216900
  gini_index: 0.4064
  vacancy_rate: 4.87
  race_white: 88615
  race_black: 7502
  race_asian: 2416
  race_native: 302
  hispanic: 6891
  bachelors_plus: 32023
districts:
  - to: "us/states/mi/districts/07"
    rel: in-district
    area_weight: 0.8387
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 0.1613
  - to: "us/states/mi/districts/senate/21"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mi/districts/house/76"
    rel: in-district
    area_weight: 0.7329
  - to: "us/states/mi/districts/house/78"
    rel: in-district
    area_weight: 0.1896
  - to: "us/states/mi/districts/house/43"
    rel: in-district
    area_weight: 0.0631
  - to: "us/states/mi/districts/house/77"
    rel: in-district
    area_weight: 0.0143
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Eaton County, MI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 109130 |
| Under 18 | 22348 |
| 18–64 | 64842 |
| 65+ | 21940 |
| Median household income | 79597 |
| Poverty rate | 8.33 |
| Homeownership rate | 74.17 |
| Unemployment rate | 4.53 |
| Median home value | 216900 |
| Gini index | 0.4064 |
| Vacancy rate | 4.87 |
| White | 88615 |
| Black | 7502 |
| Asian | 2416 |
| Native | 302 |
| Hispanic/Latino | 6891 |
| Bachelor's or higher | 32023 |

## Districts

- [MI-07](/us/states/mi/districts/07.md) — 84% (congressional)
- [MI-02](/us/states/mi/districts/02.md) — 16% (congressional)
- [MI Senate District 21](/us/states/mi/districts/senate/21.md) — 100% (state senate)
- [MI House District 76](/us/states/mi/districts/house/76.md) — 73% (state house)
- [MI House District 78](/us/states/mi/districts/house/78.md) — 19% (state house)
- [MI House District 43](/us/states/mi/districts/house/43.md) — 6% (state house)
- [MI House District 77](/us/states/mi/districts/house/77.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
