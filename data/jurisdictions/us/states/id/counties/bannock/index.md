---
type: Jurisdiction
title: "Bannock County, ID"
classification: county
fips: "16005"
state: "ID"
demographics:
  population: 89454
  population_under_18: 22469
  population_18_64: 53277
  population_65_plus: 13708
  median_household_income: 66499
  poverty_rate: 12.3
  homeownership_rate: 69.52
  unemployment_rate: 4.33
  median_home_value: 300700
  gini_index: 0.4462
  vacancy_rate: 7.13
  race_white: 74335
  race_black: 832
  race_asian: 1412
  race_native: 2300
  hispanic: 8869
  bachelors_plus: 24149
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/id/districts/senate/28"
    rel: in-district
    area_weight: 0.7367
  - to: "us/states/id/districts/senate/35"
    rel: in-district
    area_weight: 0.2295
  - to: "us/states/id/districts/senate/29"
    rel: in-district
    area_weight: 0.0336
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Bannock County, ID

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 89454 |
| Under 18 | 22469 |
| 18–64 | 53277 |
| 65+ | 13708 |
| Median household income | 66499 |
| Poverty rate | 12.3 |
| Homeownership rate | 69.52 |
| Unemployment rate | 4.33 |
| Median home value | 300700 |
| Gini index | 0.4462 |
| Vacancy rate | 7.13 |
| White | 74335 |
| Black | 832 |
| Asian | 1412 |
| Native | 2300 |
| Hispanic/Latino | 8869 |
| Bachelor's or higher | 24149 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 28](/us/states/id/districts/senate/28.md) — 74% (state senate)
- [ID Senate District 35](/us/states/id/districts/senate/35.md) — 23% (state senate)
- [ID Senate District 29](/us/states/id/districts/senate/29.md) — 3% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
