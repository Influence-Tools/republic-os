---
type: Jurisdiction
title: "Madison County, ID"
classification: county
fips: "16065"
state: "ID"
demographics:
  population: 54618
  population_under_18: 11054
  population_18_64: 40619
  population_65_plus: 2945
  median_household_income: 60160
  poverty_rate: 24.48
  homeownership_rate: 40.24
  unemployment_rate: 8.27
  median_home_value: 414800
  gini_index: 0.4942
  vacancy_rate: 12.01
  race_white: 47573
  race_black: 555
  race_asian: 816
  race_native: 134
  hispanic: 5369
  bachelors_plus: 10084
districts:
  - to: "us/states/id/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/id/districts/senate/34"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, id]
timestamp: "2026-07-03"
---

# Madison County, ID

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 54618 |
| Under 18 | 11054 |
| 18–64 | 40619 |
| 65+ | 2945 |
| Median household income | 60160 |
| Poverty rate | 24.48 |
| Homeownership rate | 40.24 |
| Unemployment rate | 8.27 |
| Median home value | 414800 |
| Gini index | 0.4942 |
| Vacancy rate | 12.01 |
| White | 47573 |
| Black | 555 |
| Asian | 816 |
| Native | 134 |
| Hispanic/Latino | 5369 |
| Bachelor's or higher | 10084 |

## Districts

- [ID-02](/us/states/id/districts/02.md) — 100% (congressional)
- [ID Senate District 34](/us/states/id/districts/senate/34.md) — 100% (state senate)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
