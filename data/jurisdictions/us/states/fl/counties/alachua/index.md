---
type: Jurisdiction
title: "Alachua County, FL"
classification: county
fips: "12001"
state: "FL"
demographics:
  population: 291782
  population_under_18: 69927
  population_18_64: 120856
  population_65_plus: 100999
  median_household_income: 65033
  poverty_rate: 23.89
  homeownership_rate: 53.7
  unemployment_rate: 4.3
  median_home_value: 329000
  gini_index: 0.5099
  vacancy_rate: 4.06
  race_white: 178602
  race_black: 47111
  race_asian: 18849
  race_native: 545
  hispanic: 38536
  bachelors_plus: 144818
districts:
  - to: "us/states/fl/districts/03"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/fl/districts/senate/6"
    rel: in-district
    area_weight: 0.5104
  - to: "us/states/fl/districts/senate/9"
    rel: in-district
    area_weight: 0.4895
  - to: "us/states/fl/districts/house/21"
    rel: in-district
    area_weight: 0.3922
  - to: "us/states/fl/districts/house/10"
    rel: in-district
    area_weight: 0.3712
  - to: "us/states/fl/districts/house/22"
    rel: in-district
    area_weight: 0.2365
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Alachua County, FL

County jurisdiction — 67 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 291782 |
| Under 18 | 69927 |
| 18–64 | 120856 |
| 65+ | 100999 |
| Median household income | 65033 |
| Poverty rate | 23.89 |
| Homeownership rate | 53.7 |
| Unemployment rate | 4.3 |
| Median home value | 329000 |
| Gini index | 0.5099 |
| Vacancy rate | 4.06 |
| White | 178602 |
| Black | 47111 |
| Asian | 18849 |
| Native | 545 |
| Hispanic/Latino | 38536 |
| Bachelor's or higher | 144818 |

## Districts

- [FL-03](/us/states/fl/districts/03.md) — 100% (congressional)
- [FL Senate District 6](/us/states/fl/districts/senate/6.md) — 51% (state senate)
- [FL Senate District 9](/us/states/fl/districts/senate/9.md) — 49% (state senate)
- [FL House District 21](/us/states/fl/districts/house/21.md) — 39% (state house)
- [FL House District 10](/us/states/fl/districts/house/10.md) — 37% (state house)
- [FL House District 22](/us/states/fl/districts/house/22.md) — 24% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
