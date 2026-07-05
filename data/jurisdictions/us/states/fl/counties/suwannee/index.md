---
type: Jurisdiction
title: "Suwannee County, FL"
classification: county
fips: "12121"
state: "FL"
demographics:
  population: 45342
  population_under_18: 9471
  population_18_64: 26244
  population_65_plus: 9627
  median_household_income: 56658
  poverty_rate: 14.97
  homeownership_rate: 74.93
  unemployment_rate: 6.28
  median_home_value: 171600
  gini_index: 0.4445
  vacancy_rate: 16.0
  race_white: 33600
  race_black: 4406
  race_asian: 302
  race_native: 111
  hispanic: 5348
  bachelors_plus: 7416
districts:
  - to: "us/states/fl/districts/03"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/fl/districts/senate/3"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/fl/districts/house/7"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Suwannee County, FL

County jurisdiction — 27 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 45342 |
| Under 18 | 9471 |
| 18–64 | 26244 |
| 65+ | 9627 |
| Median household income | 56658 |
| Poverty rate | 14.97 |
| Homeownership rate | 74.93 |
| Unemployment rate | 6.28 |
| Median home value | 171600 |
| Gini index | 0.4445 |
| Vacancy rate | 16.0 |
| White | 33600 |
| Black | 4406 |
| Asian | 302 |
| Native | 111 |
| Hispanic/Latino | 5348 |
| Bachelor's or higher | 7416 |

## Districts

- [FL-03](/us/states/fl/districts/03.md) — 100% (congressional)
- [FL Senate District 3](/us/states/fl/districts/senate/3.md) — 100% (state senate)
- [FL House District 7](/us/states/fl/districts/house/7.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
