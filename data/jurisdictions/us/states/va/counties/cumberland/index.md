---
type: Jurisdiction
title: "Cumberland County, VA"
classification: county
fips: "51049"
state: "VA"
demographics:
  population: 9818
  population_under_18: 1919
  population_18_64: 5587
  population_65_plus: 2312
  median_household_income: 55325
  poverty_rate: 8.54
  homeownership_rate: 75.94
  unemployment_rate: 3.29
  median_home_value: 239300
  gini_index: 0.4838
  vacancy_rate: 15.33
  race_white: 6290
  race_black: 2887
  race_asian: 0
  race_native: 5
  hispanic: 201
  bachelors_plus: 2103
districts:
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/10"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/va/districts/house/56"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Cumberland County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9818 |
| Under 18 | 1919 |
| 18–64 | 5587 |
| 65+ | 2312 |
| Median household income | 55325 |
| Poverty rate | 8.54 |
| Homeownership rate | 75.94 |
| Unemployment rate | 3.29 |
| Median home value | 239300 |
| Gini index | 0.4838 |
| Vacancy rate | 15.33 |
| White | 6290 |
| Black | 2887 |
| Asian | 0 |
| Native | 5 |
| Hispanic/Latino | 201 |
| Bachelor's or higher | 2103 |

## Districts

- [VA-05](/us/states/va/districts/05.md) — 100% (congressional)
- [VA Senate District 10](/us/states/va/districts/senate/10.md) — 100% (state senate)
- [VA House District 56](/us/states/va/districts/house/56.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
