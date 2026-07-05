---
type: Jurisdiction
title: "Estill County, KY"
classification: county
fips: "21065"
state: "KY"
demographics:
  population: 14035
  population_under_18: 2984
  population_18_64: 8302
  population_65_plus: 2749
  median_household_income: 46051
  poverty_rate: 20.74
  homeownership_rate: 70.41
  unemployment_rate: 7.02
  median_home_value: 119500
  gini_index: 0.4457
  vacancy_rate: 12.95
  race_white: 13488
  race_black: 10
  race_asian: 140
  race_native: 5
  hispanic: 132
  bachelors_plus: 1677
districts:
  - to: "us/states/ky/districts/06"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/ky/districts/senate/30"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ky/districts/house/91"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Estill County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14035 |
| Under 18 | 2984 |
| 18–64 | 8302 |
| 65+ | 2749 |
| Median household income | 46051 |
| Poverty rate | 20.74 |
| Homeownership rate | 70.41 |
| Unemployment rate | 7.02 |
| Median home value | 119500 |
| Gini index | 0.4457 |
| Vacancy rate | 12.95 |
| White | 13488 |
| Black | 10 |
| Asian | 140 |
| Native | 5 |
| Hispanic/Latino | 132 |
| Bachelor's or higher | 1677 |

## Districts

- [KY-06](/us/states/ky/districts/06.md) — 100% (congressional)
- [KY Senate District 30](/us/states/ky/districts/senate/30.md) — 100% (state senate)
- [KY House District 91](/us/states/ky/districts/house/91.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
