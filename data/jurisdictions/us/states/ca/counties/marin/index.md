---
type: Jurisdiction
title: "Marin County, CA"
classification: county
fips: "06041"
state: "CA"
demographics:
  population: 257969
  population_under_18: 49986
  population_18_64: 146638
  population_65_plus: 61345
  median_household_income: 149091
  poverty_rate: 8.31
  homeownership_rate: 64.66
  unemployment_rate: 6.09
  median_home_value: 1507300
  gini_index: 0.5216
  vacancy_rate: 8.11
  race_white: 174615
  race_black: 5670
  race_asian: 16031
  race_native: 1871
  hispanic: 50216
  bachelors_plus: 168335
districts:
  - to: "us/states/ca/districts/02"
    rel: in-district
    area_weight: 0.6558
  - to: "us/states/ca/districts/senate/2"
    rel: in-district
    area_weight: 0.6559
  - to: "us/states/ca/districts/house/12"
    rel: in-district
    area_weight: 0.6559
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Marin County, CA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 257969 |
| Under 18 | 49986 |
| 18–64 | 146638 |
| 65+ | 61345 |
| Median household income | 149091 |
| Poverty rate | 8.31 |
| Homeownership rate | 64.66 |
| Unemployment rate | 6.09 |
| Median home value | 1507300 |
| Gini index | 0.5216 |
| Vacancy rate | 8.11 |
| White | 174615 |
| Black | 5670 |
| Asian | 16031 |
| Native | 1871 |
| Hispanic/Latino | 50216 |
| Bachelor's or higher | 168335 |

## Districts

- [CA-02](/us/states/ca/districts/02.md) — 66% (congressional)
- [CA Senate District 2](/us/states/ca/districts/senate/2.md) — 66% (state senate)
- [CA House District 12](/us/states/ca/districts/house/12.md) — 66% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
