---
type: Jurisdiction
title: "Crawford County, MO"
classification: county
fips: "29055"
state: "MO"
demographics:
  population: 22797
  population_under_18: 5062
  population_18_64: 12878
  population_65_plus: 4857
  median_household_income: 57629
  poverty_rate: 14.05
  homeownership_rate: 69.24
  unemployment_rate: 4.87
  median_home_value: 172600
  gini_index: 0.4728
  vacancy_rate: 16.08
  race_white: 21127
  race_black: 177
  race_asian: 18
  race_native: 42
  hispanic: 552
  bachelors_plus: 2969
districts:
  - to: "us/states/mo/districts/03"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/mo/districts/senate/3"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/mo/districts/house/120"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Crawford County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 22797 |
| Under 18 | 5062 |
| 18–64 | 12878 |
| 65+ | 4857 |
| Median household income | 57629 |
| Poverty rate | 14.05 |
| Homeownership rate | 69.24 |
| Unemployment rate | 4.87 |
| Median home value | 172600 |
| Gini index | 0.4728 |
| Vacancy rate | 16.08 |
| White | 21127 |
| Black | 177 |
| Asian | 18 |
| Native | 42 |
| Hispanic/Latino | 552 |
| Bachelor's or higher | 2969 |

## Districts

- [MO-03](/us/states/mo/districts/03.md) — 100% (congressional)
- [MO Senate District 3](/us/states/mo/districts/senate/3.md) — 100% (state senate)
- [MO House District 120](/us/states/mo/districts/house/120.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
