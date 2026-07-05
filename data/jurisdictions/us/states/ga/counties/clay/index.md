---
type: Jurisdiction
title: "Clay County, GA"
classification: county
fips: "13061"
state: "GA"
demographics:
  population: 2850
  population_under_18: 562
  population_18_64: 1457
  population_65_plus: 831
  median_household_income: 49147
  poverty_rate: 21.02
  homeownership_rate: 78.31
  unemployment_rate: 4.5
  median_home_value: 94400
  gini_index: 0.4406
  vacancy_rate: 37.86
  race_white: 1063
  race_black: 1725
  race_asian: 0
  race_native: 1
  hispanic: 0
  bachelors_plus: 717
districts:
  - to: "us/states/ga/districts/02"
    rel: in-district
    area_weight: 0.9931
  - to: "us/states/al/districts/01"
    rel: in-district
    area_weight: 0.0064
  - to: "us/states/ga/districts/house/154"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Clay County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2850 |
| Under 18 | 562 |
| 18–64 | 1457 |
| 65+ | 831 |
| Median household income | 49147 |
| Poverty rate | 21.02 |
| Homeownership rate | 78.31 |
| Unemployment rate | 4.5 |
| Median home value | 94400 |
| Gini index | 0.4406 |
| Vacancy rate | 37.86 |
| White | 1063 |
| Black | 1725 |
| Asian | 0 |
| Native | 1 |
| Hispanic/Latino | 0 |
| Bachelor's or higher | 717 |

## Districts

- [GA-02](/us/states/ga/districts/02.md) — 99% (congressional)
- [AL-01](/us/states/al/districts/01.md) — 1% (congressional)
- [GA House District 154](/us/states/ga/districts/house/154.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
