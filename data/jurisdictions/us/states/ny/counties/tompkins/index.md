---
type: Jurisdiction
title: "Tompkins County, NY"
classification: county
fips: "36109"
state: "NY"
demographics:
  population: 104537
  population_under_18: 14745
  population_18_64: 72798
  population_65_plus: 16994
  median_household_income: 74024
  poverty_rate: 16.36
  homeownership_rate: 54.14
  unemployment_rate: 5.54
  median_home_value: 290900
  gini_index: 0.4829
  vacancy_rate: 9.5
  race_white: 78663
  race_black: 4358
  race_asian: 10646
  race_native: 266
  hispanic: 6886
  bachelors_plus: 57264
districts:
  - to: "us/states/ny/districts/19"
    rel: in-district
    area_weight: 0.9968
  - to: "us/states/ny/districts/senate/52"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ny/districts/house/125"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Tompkins County, NY

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 104537 |
| Under 18 | 14745 |
| 18–64 | 72798 |
| 65+ | 16994 |
| Median household income | 74024 |
| Poverty rate | 16.36 |
| Homeownership rate | 54.14 |
| Unemployment rate | 5.54 |
| Median home value | 290900 |
| Gini index | 0.4829 |
| Vacancy rate | 9.5 |
| White | 78663 |
| Black | 4358 |
| Asian | 10646 |
| Native | 266 |
| Hispanic/Latino | 6886 |
| Bachelor's or higher | 57264 |

## Districts

- [NY-19](/us/states/ny/districts/19.md) — 100% (congressional)
- [NY Senate District 52](/us/states/ny/districts/senate/52.md) — 100% (state senate)
- [NY House District 125](/us/states/ny/districts/house/125.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
