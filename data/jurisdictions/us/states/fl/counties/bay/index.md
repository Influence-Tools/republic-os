---
type: Jurisdiction
title: "Bay County, FL"
classification: county
fips: "12005"
state: "FL"
demographics:
  population: 199718
  population_under_18: 46003
  population_18_64: 66173
  population_65_plus: 87542
  median_household_income: 78061
  poverty_rate: 10.7
  homeownership_rate: 65.59
  unemployment_rate: 5.5
  median_home_value: 343300
  gini_index: 0.4344
  vacancy_rate: 24.69
  race_white: 149447
  race_black: 14457
  race_asian: 4823
  race_native: 1630
  hispanic: 21076
  bachelors_plus: 57864
districts:
  - to: "us/states/fl/districts/02"
    rel: in-district
    area_weight: 0.6026
  - to: "us/states/fl/districts/senate/2"
    rel: in-district
    area_weight: 0.6024
  - to: "us/states/fl/districts/house/6"
    rel: in-district
    area_weight: 0.6024
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Bay County, FL

County jurisdiction — 50 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 199718 |
| Under 18 | 46003 |
| 18–64 | 66173 |
| 65+ | 87542 |
| Median household income | 78061 |
| Poverty rate | 10.7 |
| Homeownership rate | 65.59 |
| Unemployment rate | 5.5 |
| Median home value | 343300 |
| Gini index | 0.4344 |
| Vacancy rate | 24.69 |
| White | 149447 |
| Black | 14457 |
| Asian | 4823 |
| Native | 1630 |
| Hispanic/Latino | 21076 |
| Bachelor's or higher | 57864 |

## Districts

- [FL-02](/us/states/fl/districts/02.md) — 60% (congressional)
- [FL Senate District 2](/us/states/fl/districts/senate/2.md) — 60% (state senate)
- [FL House District 6](/us/states/fl/districts/house/6.md) — 60% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
