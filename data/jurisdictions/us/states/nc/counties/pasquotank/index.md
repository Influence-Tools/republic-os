---
type: Jurisdiction
title: "Pasquotank County, NC"
classification: county
fips: "37139"
state: "NC"
demographics:
  population: 40834
  population_under_18: 8737
  population_18_64: 24485
  population_65_plus: 7612
  median_household_income: 66589
  poverty_rate: 11.04
  homeownership_rate: 67.49
  unemployment_rate: 5.85
  median_home_value: 234600
  gini_index: 0.4396
  vacancy_rate: 10.92
  race_white: 22478
  race_black: 14163
  race_asian: 572
  race_native: 198
  hispanic: 2469
  bachelors_plus: 10250
districts:
  - to: "us/states/nc/districts/01"
    rel: in-district
    area_weight: 0.8047
  - to: "us/states/nc/districts/senate/1"
    rel: in-district
    area_weight: 0.8001
  - to: "us/states/nc/districts/house/5"
    rel: in-district
    area_weight: 0.8
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Pasquotank County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 40834 |
| Under 18 | 8737 |
| 18–64 | 24485 |
| 65+ | 7612 |
| Median household income | 66589 |
| Poverty rate | 11.04 |
| Homeownership rate | 67.49 |
| Unemployment rate | 5.85 |
| Median home value | 234600 |
| Gini index | 0.4396 |
| Vacancy rate | 10.92 |
| White | 22478 |
| Black | 14163 |
| Asian | 572 |
| Native | 198 |
| Hispanic/Latino | 2469 |
| Bachelor's or higher | 10250 |

## Districts

- [NC-01](/us/states/nc/districts/01.md) — 80% (congressional)
- [NC Senate District 1](/us/states/nc/districts/senate/1.md) — 80% (state senate)
- [NC House District 5](/us/states/nc/districts/house/5.md) — 80% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
