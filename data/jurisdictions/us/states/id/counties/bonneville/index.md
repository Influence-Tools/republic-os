---
type: Jurisdiction
title: "Bonneville County, ID"
classification: county
fips: "16019"
state: "ID"
demographics:
  population: 129523
  population_under_18: 38603
  population_18_64: 72970
  population_65_plus: 17950
  median_household_income: 79068
  poverty_rate: 9.77
  homeownership_rate: 71.74
  unemployment_rate: 4.57
  median_home_value: 368800
  gini_index: 0.4251
  vacancy_rate: 6.96
  race_white: 109136
  race_black: 566
  race_asian: 1181
  race_native: 1058
  hispanic: 18769
  bachelors_plus: 34605
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/id/districts/senate/35"
    rel: in-district
    area_weight: 0.7954
  - to: "us/states/id/districts/senate/32"
    rel: in-district
    area_weight: 0.1952
  - to: "us/states/id/districts/senate/33"
    rel: in-district
    area_weight: 0.0093
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Bonneville County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 129523 |
| Under 18 | 38603 |
| 18–64 | 72970 |
| 65+ | 17950 |
| Median household income | 79068 |
| Poverty rate | 9.77 |
| Homeownership rate | 71.74 |
| Unemployment rate | 4.57 |
| Median home value | 368800 |
| Gini index | 0.4251 |
| Vacancy rate | 6.96 |
| White | 109136 |
| Black | 566 |
| Asian | 1181 |
| Native | 1058 |
| Hispanic/Latino | 18769 |
| Bachelor's or higher | 34605 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 35](/us/states/id/districts/senate/35.md) — 80% (state senate)
- [ID Senate District 32](/us/states/id/districts/senate/32.md) — 20% (state senate)
- [ID Senate District 33](/us/states/id/districts/senate/33.md) — 1% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
